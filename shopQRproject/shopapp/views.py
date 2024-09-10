from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import *
from .utils import *

# Create your views here.

def Home(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        if data:
            data = data.lower()
            # Assuming 'data' contains the URL part you want to append
            url = f'http://127.0.0.1:8000/instore/{data}'
            qr_code_image = generate_qr_code(url)
            qr_code = QRCode.objects.create(data=url, image=qr_code_image)
            qr_code.save()
            context = {'qr_code': qr_code}
            return render(request, 'qrdisplay.html', context)
    return render(request,'index.html')

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from Products.models import *
import random


def InstoreProduct(request, slug):
    product = get_object_or_404(Product, slug=slug)
        # Giving out 50%  discount of the original product price
    product.initial_price = product.price * 0.2 + product.price
    
    # Fetch 4 random products
    related_products = Product.objects.filter(Category=product.Category).exclude(pk=product.pk).order_by('?')[:4]
    for related_product in related_products:
        # Giving out 50% discount of the original product price
        related_product.initial_price = related_product.price * 0.2 + related_product.price
        
    context = {"product": product, "pin": product.get_pin(),"related_products":related_products}
    return render(request, 'Instore/instoreProduct.html', context)


@login_required
def cheese_view(request):
    print(request.user.is_authenticated)  # Should print True for logged-in users
    return render(request, 'cheese.html')


@login_required
def QRdisplay(request):
    return render(request, 'qrdisplay.html')
@login_required
def QRscanner(request):
    return render(request, 'Instore/qrscanner.html')

def Products(request):
    return render(request, 'products.html')

# def Welcome(request):
#     return render(request, 'Homepages/welcome.html')

from django.shortcuts import render
from django.contrib.auth.models import User

# def Option(request):
#     user = User.objects.get(username=request.user.username)
#     context = {"user": user}
#     return render(request, 'Homepages/option.html', context)

def InstoreCart(request):
    return render(request, 'Instore/instorecart.html')

