from django import forms
from django.forms import ModelForm, inlineformset_factory, BaseInlineFormSet
from .models import Product, Stock

class ProductForm(forms.ModelForm): # 매장 관리자용 상품 등록 폼
    class Meta:
        model = Product
        # fields = ['product_id', 'product_name']
        fields = '__all__'

class StockForm(forms.ModelForm): # 매장 관리자용 재고 등록 폼
    class Meta:
        model = Stock
        fields = ['product', 'stock']
