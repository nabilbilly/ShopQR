from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem
from Products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def view_cart(request):
    # Get or create the cart for the logged-in user
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Fetch cart items for this cart
    cart_items = CartItem.objects.filter(cart=cart)
    
    # Calculate total price
    total_price = sum(item.item_price for item in cart_items)
    cart.total_price = total_price
    cart.save()
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'Instore/cart_view.html', context)

@login_required
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += int(request.POST.get('quantity', 1))
        cart_item.save()
    return redirect('view_cart')

@login_required
def update_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    
    if request.method == 'POST':
        for item in cart.items.all():
            slug = item.product.slug  # Using the product's slug
            quantity = request.POST.get(f'quantity_{slug}')
            
            if quantity and int(quantity) > 0:
                item.quantity = int(quantity)
                item.save()
    
    return redirect('view_cart')

@login_required
def remove_from_cart(request, slug):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product__slug=slug)  # Use slug to find the cart item
    cart_item.delete()
    
    return redirect('view_cart')


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import * # Import your models
from django.utils import timezone

def receipt_view(request):
    receipt_uid = request.GET.get('receipt_uid')  # Fetch the receipt UUID from the query parameter
    
    if not receipt_uid:
        return render(request, 'Instore/receipt.html', {'error': 'No receipt UUID provided.'})
    
    receipt = get_object_or_404(Receipt, uid=receipt_uid)
    
    return render(request, 'Instore/receipt.html', {
        'receipt': receipt,
        'cart_items': receipt.cart_items,  # Use cart items stored in the receipt
        'total_price': receipt.total_price,
        'username': receipt.user.username,
        'receipt_date': receipt.receipt_date
    })

@login_required
def generate_receipt(request):
    if request.method == 'POST':
        user = request.user
        cart = Cart.objects.filter(user=user).first()

        if not cart:
            return JsonResponse({'success': False, 'message': 'Cart not found'})

        try:
            # Create the receipt
            receipt = Receipt.objects.create(
                user=user,
                total_price=cart.total_price,
                cart_items=[{
                    'product': item.product.product_name,  # Assuming the product name is what you want
                    'quantity': item.quantity,
                    'price': float(item.item_price),  # Convert Decimal to float
                    'image': item.product.product_images.first().image.url if item.product.product_images.exists() else None
                } for item in cart.items.all()]
            )
            # Save receipt details in history
            receipt_history = ReceiptHistory.objects.create(
                user=user,
                receipt_uid=receipt.uid,
                total_price=cart.total_price,
            )

            # Save each cart item to CartItemHistory
            for item in cart.items.all():
                CartItemHistory.objects.create(
                    user=user,
                    product_name=item.product.product_name,
                    quantity=item.quantity,
                    price=item.item_price,
                    purchase_date=timezone.now()
                )
            
            # Clear the cart after creating the receipt
            cart.items.all().delete()

            return JsonResponse({
                'success': True,
                'receipt_uid': str(receipt.uid)  # Send the UUID of the receipt
            })

        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})


@login_required
def cart_items_history(request):
    user = request.user
    history_items = CartItemHistory.objects.filter(user=user).order_by('-purchase_date')
    return render(request, 'Instore/cart_history.html', {'history_items': history_items})



@login_required
def receipt_history(request):
    user = request.user
    receipt_items = ReceiptHistory.objects.filter(user=user).order_by('-purchase_date')
    return render(request, 'Instore/receipt_history.html', {'receipt_items': receipt_items})





















