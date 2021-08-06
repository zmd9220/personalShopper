from django import forms
from .models import Product, Stock

class ProductForm(forms.ModelForm): # 매장 관리자용 상품 등록 폼
    class Meta:
        model = Product
        fields = ['product_id', 'product_name']

class StockForm(forms.ModelForm): # 매장 관리자용 재고 등록 폼
    class Meta:
        model = Stock
        fields = ['product', 'size', 'stock']