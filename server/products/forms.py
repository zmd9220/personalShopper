from django import forms
from .models import Product, Stock

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name']

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'size', 'stock']