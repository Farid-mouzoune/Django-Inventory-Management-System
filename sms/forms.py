from django import forms
from .models import Stock


class StockAdminFormView(forms.ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"


class StockFormView(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'description', 'price']


class TagAdminFormView(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name']
