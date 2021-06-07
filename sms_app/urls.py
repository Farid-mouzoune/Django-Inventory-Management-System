from django.urls import path
from . import views


app_name = 'sms_app'
urlpatterns = [
    path('', views.all_stock, name='home'),
    path('stocks', views.all_stock, name='all_stock'),
    path('stock/<str:id>', views.get_stock, name='get_stock'),
    path('add/stock', views.add_stock, name='add_stock'),
    path('update/stock/<str:id>', views.update_stock, name='update_stock'),
    path('delete/stock/<str:id>', views.delete_stock, name='delete_stock'),
    path('export-pdf', views.export_pdf, name='export-pdf'),
    # path('export-csv', views.export_csv, name='export-csv'),
    path('dashboard', views.dashboard, name='dashboard'),
    # path('404', views.error_404, name='404'),


    # path('profile', views.profile, name='profile'),
    # path('edit', UserEditView.as_view(), name='profile_edit'),

]

