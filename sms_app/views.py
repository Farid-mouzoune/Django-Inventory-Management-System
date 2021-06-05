from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Stock
from .forms import StockFormView
# Create your views here.


def dashboard(request):
    return render(request, 'sms_app/dashboard.html')


def all_stock(request):
    stock = Stock.objects.all().order_by('-date_created')
    title = 'Inventory'
    content = 'This page represent all products stocked in our inventory'
    return render(request, 'sms_app/all_stock.html', {'all_stock': stock, 'title': title, 'content': content})


def add_stock(request):
    form = StockFormView(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/stocks')
    else:
        form = StockFormView(request.POST, request.FILES)
    title = 'Add Item'
    content = "Let's Add an item to your inventory"
    context = {'form': form, 'title': title, 'content': content}
    return render(request, 'sms_app/add_stock.html', context)


