from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
# from .models import Cart, CartItem, Product
from django.contrib.auth.decorators import login_required
from Products.models import *
import random




def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product.initial_price = product.price * 1.2
    related_products = Product.objects.filter(Category=product.Category).exclude(pk=product.pk).order_by('?')[:4]
    for related_product in related_products:
        related_product.initial_price = related_product.price * 1.2
    
    context = {
        "product": product,
        "pin": product.get_pin(),
        "related_products": related_products,
    }
    return render(request, 'Product/product.html', context)




