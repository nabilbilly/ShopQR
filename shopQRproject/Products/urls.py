from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.product, name='paticularproduct'),
     
]

# urlpatterns = [
#     path('<slug:slug>/', views.product, name='product_detail'),
    
   
# ]


#    path('product/add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
#    path('cart/', views.cart_view, name='cart_view'),
#    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
#    path('<slug:slug>/', views.product, name='product_detail'),
# ]