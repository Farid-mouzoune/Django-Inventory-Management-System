from django.shortcuts import render
from django.http import HttpResponse
from .models import Stock
from .forms import StockFormView
# Create your views here.


def home(request):
    return HttpResponse('hello')


def all_stock(request):
    stock = Stock.objects.all()
    return render(request, 'sms/all_stock.html', {'all_stock': stock})


def add_stock(request):
    form = StockFormView(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'sms/add_stock.html', context)


