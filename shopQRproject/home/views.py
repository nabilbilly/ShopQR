from django.shortcuts import render,redirect
from Products.models import *
import random


def landing_page(request):
    
    products = list(Product.objects.all().order_by('?')[:4])
    random.shuffle(products)
    for product in products:
        # Giving out 50%  discount of the original product price
        product.initial_price = product.price * 0.2 + product.price
        
    productsa = list(Product.objects.all().order_by('?')[:12])
    random.shuffle(productsa)
    for product in productsa:
        # Giving out 50%  discount of the original product price
        product.initial_price = product.price * 0.2 + product.price
        
    context = {'products': products, "productsa": productsa}
   
    return render(request, 'Onlinestore/landing.html', context)



# def landing_page(request):
#     products = Product.objects.all().order_by('-created_at')[:4]    Edited 2 : Help retrive only the first four product
#     products = list(Product.objects.all().order_by('?')[:4])
#     random.shuffle(products)
#     context = {'products': products}
#     # context = {'products': Product.objects.all()}  # Edited 1 :Help retrive all products 
#     return render(request, 'home/landing.html', context)

