# cart/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.view_cart, name='view_cart'),
#     path('add/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('cart/update/', views.update_cart, name='update_cart'),
    path('generate-receipt/', views.generate_receipt, name='generate_receipt'),  # For generating receipt
    path('receipt/', views.receipt_view, name='receipt'),  # For viewing receipt
    path('history/cart/', views.cart_items_history, name='cart_items_history'),
    path('history/receipts/', views.receipt_history, name='receipt_history'),
    # path('payment/success/<uuid:cart_id>/', views.payment_success, name='payment_success'),
    # path('receipt/<uuid:receipt_id>/', views.receipt_view, name='receipt_view'),
    path('add/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<slug:slug>/', views.remove_from_cart, name='remove_from_cart'),
]

