from django import forms
from .models import Stock


class StockAdminFormView(forms.ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"


class TagAdminFormView(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name']


class StockFormView(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'description', 'category', 'price', 'quantity', 'receive_quantity', 'quantity_required',
                  'receive_by', 'image', 'tags_id']
        # fields = "__all__"


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'description', 'price', 'receive_quantity', 'quantity',
                  'receive_by', 'image', 'tags_id']


class StockSearchForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'quantity', 'export_to_csv']


class StockReceiveQuantityForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['receive_quantity']


class StockQuantityRequiredForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['quantity_required']
