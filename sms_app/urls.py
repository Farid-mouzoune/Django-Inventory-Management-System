from django.urls import path
from . import views


app_name = 'sms_app'
urlpatterns = [
    path('', views.all_stock, name='home'),
    path('stocks', views.all_stock, name='all_stock'),
    path('stock/<str:id>/', views.get_stock, name='get_stock'),
    path('receive_quantity/<str:id>/', views.receive_quantity, name='receive_quantity'),
    path('quantity_required/<str:id>/', views.quantity_required, name='quantity_required'),
    path('add/stock', views.add_stock, name='add_stock'),
    path('update/stock/<str:id>', views.update_stock, name='update_stock'),
    path('delete/stock/<str:id>', views.delete_stock, name='delete_stock'),
    path('reorder_level/<str:id>', views.reorder_level, name='reorder_level'),
    path('export-pdf', views.export_pdf, name='export-pdf'),
    path('export-excel', views.export_excel, name='export-excel'),
    # path('export-csv', views.export_csv, name='export-csv'),
    path('dashboard', views.dashboard, name='dashboard'),

]

