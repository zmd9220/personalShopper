from django.contrib import admin
from .models import Product, Stock
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name' ]

class StockAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'stock' ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)