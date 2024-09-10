from django.contrib import admin

# Register your models here.
from .models import *
from base.models import *

# admin.site.register(Cart)
# admin.site.register(CartItem)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'item_price')

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'receipt_date','cart_items')

# Register your models here.
@admin.register(CartItemHistory)
class CartItemHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_name', 'quantity', 'price', 'purchase_date')
    search_fields = ('user__username', 'product_name')

@admin.register(ReceiptHistory)
class ReceiptHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'receipt_uid', 'total_price', 'purchase_date')
    search_fields = ('user__username', 'receipt_uid')