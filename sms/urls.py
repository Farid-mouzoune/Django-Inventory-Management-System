from django.urls import path
from . import views


app_name = 'sms'
urlpatterns = [
    path('', views.home, name='home'),
    path('stocks', views.all_stock, name='all_stock'),
    path('add/stock', views.add_stock, name='add_stock'),


    # path('profile', views.profile, name='profile'),
    # path('edit', UserEditView.as_view(), name='profile_edit'),

]

