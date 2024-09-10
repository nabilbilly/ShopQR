from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Welcome, name='Welcome'),
    # path('option/', views.Option, name='Option'),
    path('scanner/', views.QRscanner, name='QRscanner'),
    path('InstoreCart/', views.InstoreCart, name='InstoreCart'),
    path('input/', views.Home, name='home'),
    path('QR/', views.QRdisplay, name='QRdisplay'),
    path('cheese/', views.cheese_view, name='cheese_view'),
    path('product/', views.Products, name='products'),
    path('<slug:slug>/', views.InstoreProduct, name='paticularproductInstore'),  # Moved to the end
]
