from django.contrib import admin
from . import models
from .models import Product, Stock
from django.contrib import messages
# Register your models here.

class ProductAdmin(admin.ModelAdmin): # 상품정보관리
    list_display = ['product_id', 'product_name' ]

class StockAdmin(admin.ModelAdmin): # 상품재고관리
    list_display = ['product', 'stock' ]
    # list_display = ['product', 'size', 'stock' ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)

#######################

# class KioskAdminArea(admin.AdminSite):
#     site_header = 'Kiosk Database'

# class TestAdminPermissions(admin.ModelAdmin):
    
#     def has_add_permission(self, request):
#         return False
    
#     def has_change_permission(self, request, obj=None):
#         return False

#     def has_delete_permission(self, request, obj=None):
        
#         # if request.user.groups.filter(name='editors').exists():
#         #     return True
        
#         if request.POST.get('action') == 'delete_selected':
#             messages.add_message(request, messages.ERROR,(
#                 "I really hope you are sure about this!"
#             ))

#         return True

#     def has_view_permission(self, request, obj=None):
#         return True

# kiosk_admin = KioskAdminArea(name='KioskAdmin')
# kiosk_admin.register(models.Product, TestAdminPermissions)
# kiosk_admin.register(models.Stock)