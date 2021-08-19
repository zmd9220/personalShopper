from django.db import models
from .models import Product, Customer, Stock
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer): # 상품 Serializer

    class Meta:
        model = Product
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer): # 고객 Serializer

    class Meta:
        model = Customer
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer): # 재고 Serializer

    class Meta:
        model = Stock
        fields = '__all__'
