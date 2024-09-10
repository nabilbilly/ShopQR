from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django.utils.text import slugify
from base.models import *
from Products.models import *
from shopapp.models import *
from Products.PhotoResize import compress_image, save_image
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import hashlib

class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Cart - {self.user}"


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.item_price = self.product.price * self.quantity
        super(CartItem, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity}"
    
    
class Receipt(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # Add total_price field
    receipt_date = models.DateTimeField(auto_now_add=True)
    cart_items = models.JSONField(default=list)
    
    def __str__(self):
        return f"Receipt - {self.user.username} on {self.receipt_date}"
    


class CartItemHistory(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} ({self.quantity}) - ${self.price}"

class ReceiptHistory(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receipt_uid = models.UUIDField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Receipt {self.receipt_uid} - ${self.total_price}"


    
