from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django.utils.text import slugify
from base.models import *
from shopapp.models import *
from .PhotoResize import compress_image, save_image
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import hashlib

class Category(BaseModel):
    category_name= models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True )
    category_image= models.ImageField( upload_to="categories")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        self.category_image = compress_image(self.category_image)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.category_name
    
  
class ColorVariants(BaseModel):
    color_name =models.CharField(max_length=100,default="None")
    price = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.color_name
        
class SizeVariants(BaseModel):
    size_name =models.CharField(max_length=100,default="Normal")
    price = models.IntegerField(default=0) 
    
    def __str__(self) -> str:
        return self.size_name   
  
    
    
class Product(BaseModel):
    product_name = models.CharField( max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True )
    Category = models.ForeignKey( Category, on_delete= models.CASCADE, related_name= "product")
    price = models.IntegerField()
    project_description = models.TextField()
    color_variant = models.ManyToManyField(ColorVariants)
    size_variant = models.ManyToManyField(SizeVariants)
    qrCode = models.ManyToManyField(QRCode)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)
  
    def get_pin(self):
        # Use the first 8 characters of a hash of the UID
        return hashlib.md5(str(self.uid).encode('utf-8')).hexdigest()[:8]

    def __str__(self) -> str:
        return self.product_name
        
class ProductImage(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="products")
    
    
    def save(self, *args, **kwargs):
        self.image = self.resize_and_crop_image(self.image)
        super(ProductImage, self).save(*args, **kwargs)

    def resize_and_crop_image(self, image_field, target_size=(300, 300)):
        img = Image.open(image_field)
        img.thumbnail(target_size, Image.LANCZOS)  # Use LANCZOS for high-quality downsampling filter

        # Create a new image with white background
        background = Image.new('RGB', target_size, (255, 255, 255))
        img_w, img_h = img.size
        bg_w, bg_h = background.size
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
        background.paste(img, offset)

        buffer = BytesIO()
        background.save(buffer, format='JPEG')
        return ContentFile(buffer.getvalue(), image_field.name)


    def __str__(self) -> str:
        return str(self.product)
    
    
