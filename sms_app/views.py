from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Stock, Tag
from .forms import *
from django.shortcuts import get_object_or_404
import csv
import datetime
from django.db.models import Q, Sum
from django.template.loader import render_to_string
from django.contrib import messages
from weasyprint import HTML
import tempfile
import xlwt
# Create your views here.


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=stock excel' + str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Stock')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['NAME', 'QUANTITY', 'QUANTITY RECEIVED']
    for col in range(len(columns)):
        ws.write(row_num, col, columns[col], font_style)
    font_style.font.bold = xlwt.XFStyle()
    rows = Stock.objects.filter().values_list('name', 'quantity', 'receive_quantity')
    for row in rows:
        row_num += 1
        for col in range(len(row)):
            ws.write(row_num, col, str(row[col]), font_style)
    wb.save(response)
    return response


def dashboard(request):
    return render(request, 'sms_app/dashboard.html')


def all_stock(request):
    form = StockSearchForm(request.POST or None)
    stock = Stock.objects.all()
    title = 'Inventory'
    content = 'This page represent all products stocked in our inventory'
    context = {'all_stock': stock, 'title': title, 'content': content, 'form': form}
    if request.method == 'POST':
        stock = Stock.objects.filter(name__icontains=form['name'].value(),
                                     quantity__icontains=form['quantity'].value())
        context = {'all_stock': stock, 'title': title, 'content': content, 'form': form}
        if form['export_to_csv'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=list of stock' + str(datetime.datetime.now()) + '.csv'
            writer = csv.writer(response)
            writer.writerow(['NAME', 'QUANTITY', 'QUANTITY RECEIVED', 'QUANTITY ISSUE'])
            instance = stock
            for st in instance:
                writer.writerow([st.name, st.quantity, st.receive_quantity, st.issue_quantity])
            return response
    return render(request, 'sms_app/all_stock.html', context)


def export_pdf(request):
    stock = Stock.objects.all()
    sum = stock.count()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=stock pdf' + str(datetime.datetime.now()) + '.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    html_string = render_to_string('sms_app/pdf-output.html', {'stock': stock, 'total': 0})
    html = HTML(string=html_string)
    result = html.write_pdf()
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response


def name_tag(request):
    tag = Tag.objects.all()
    return render(request, 'sms_app/all_stock.html', {'tags': tag})


def add_stock(request):
    form = StockFormView(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Product was added with successfully')
        return redirect('/stocks')
    else:
        form = StockFormView(request.POST, request.FILES)
    title = 'Add Item'
    content = "Let's Add an item to your inventory"
    context = {'form': form, 'title': title, 'content': content}
    return render(request, 'sms_app/add_stock.html', context)


def get_stock(request, id):
    try:
        stock = Stock.objects.get(id=id)
    except Stock.DoesNotExist:
        return render(request, 'sms_app/404.html')
    context = {'get_stock': stock}
    return render(request, 'sms_app/get_stock.html', context)


def receive_quantity(request, id):
    queryset = Stock.objects.get(id=id)
    form = StockReceiveQuantityForm(instance=queryset)
    if request.method == 'POST':
        form = StockReceiveQuantityForm(request.POST or None, instance=queryset)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.receive_quantity = instance.receive_quantity
            instance.save()
            receiver_stock_history = StockHistory(
                id=instance.id,
                name=instance.name,
                description=instance.description,
                price=instance.price,
                quantity=instance.quantity,
                receive_quantity=instance.receive_quantity,
                quantity_required=instance.quantity_required,
                issue_quantity=instance.issue_quantity,
                issue_by=instance.issue_by,
                quantity_calc=instance.quantity_calc,
                last_updated=instance.last_updated,
            )
            receiver_stock_history.save()
            messages.success(request, f"Received Successfully  {str(instance.quantity_calc)}  {str(instance.name)}'s now in store")
            return redirect('/stock/'+str(instance.id))
    context = {
        'title': 'Receive',
        'get_stock': queryset,
        'form': form,
        'username': 'Receive by',
    }
    return render(request, 'sms_app/add_stock.html', context)


def quantity_required(request, id):

    queryset = Stock.objects.get(id=id)
    form = StockQuantityRequiredForm(instance=queryset)
    if request.method == 'POST':
        form = StockQuantityRequiredForm(request.POST or None, instance=queryset)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.quantity_required = instance.quantity_required
            instance.save()
            return redirect('/stock/'+str(instance.id))
    context = {
        'title': 'Receive',
        'get_stock': queryset,
        'form': form,
        'username': 'Receive by',
    }
    return render(request, 'sms_app/add_stock.html', context)


def update_stock(request, id):
    query = Stock.objects.get(id=id)
    form = StockUpdateForm(instance=query)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product was Updated with successfully')
            return redirect('/stocks')

    context = {'form': form}
    return render(request, 'sms_app/add_stock.html', context)


def delete_stock(request, id):
    query = Stock.objects.get(id=id)
    if request.method == 'POST':
        query.delete()
        messages.success(request, 'Product was deleted with successfully')
        return redirect('/stocks')
    return render(request, 'sms_app/delete_stock.html')


def reorder_level(request, id):
    queryset = Stock.objects.get(id=id)
    form = ReorderLevelForm(request.POST or None, instance=queryset)
    if request.method == "POST":
        if form.is_valid():
            form = ReorderLevelForm(request.POST or None, instance=queryset)
            instance = form.save(commit=False)
            instance.save()
            return redirect('/stocks')
    context = {
        'stock': queryset,
        'form': form,
    }
    return render(request, 'sms_app/add_stock.html', context)
