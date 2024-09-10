from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from base.models import *

admin.site.register(Category)

# admin.site.register(Cart)
# admin.site.register(CartItem)
# admin.site.register(BaseModel)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price']
    inlines = [ProductImageAdmin]
    
@admin.register(ColorVariants)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color_name', 'price']
    model = ColorVariants

@admin.register(SizeVariants)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size_name', 'price']
    model = SizeVariants
    
# @admin.register(QRCode)
# class QRCodeAdmin(admin.ModelAdmin):
#     list_display = ['data', 'image']
#     model = QRCode
    
admin.site.register(Product, ProductAdmin)  
admin.site.register(ProductImage)
