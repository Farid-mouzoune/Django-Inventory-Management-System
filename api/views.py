from django.shortcuts import render, redirect
from sms_app.models import Stock
from django.http import HttpResponse
# Create your views here.

# Rest Framework api
from api import serializers
from .serializers import StockSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_urls(request):
    Api_Urls = {
        'List': '/stock-list-/',
        'Detail View': '/stock-detail/<str:pk>/',
        'Create': '/stock-create/',
        'Update': '/stock-update/<str:pk>/',
        'Delete': 'stock-delete/<str:pk>/',
    }
    return Response(Api_Urls)


@api_view(['GET'])
def StockList(request):
    stock = Stock.objects.all().order_by('id')
    serializer = StockSerializers(stock, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def StockDetail(request, pk):
    stock = Stock.objects.get(id=pk)
    serializer = StockSerializers(stock, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def StockCreate(request):
    serializer = StockSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def StockUpdate(request, pk):
    stock = Stock.objects.get(id=pk)
    serializer = StockSerializers(instance=stock, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def StockDelete(request, pk):
    stock = Stock.objects.get(id=pk)
    stock.delete()
    return Response('Item was deleted Successfully')
