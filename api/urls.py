from django.urls import path
from . import views


app_name = 'api'
urlpatterns = [
    path('', views.api_urls, name='api_urls'),
    path('stock-list/', views.StockList, name='StockList'),
    path('stock-detail/<str:pk>/', views.StockDetail, name='stock-detail'),
    path('stock-create/', views.StockCreate, name='stock-create'),
    path('stock-update/<str:pk>/', views.StockUpdate, name='stock-update'),
    path('stock-delete/<str:pk>/', views.StockDelete, name='stock-delete')

    ]
