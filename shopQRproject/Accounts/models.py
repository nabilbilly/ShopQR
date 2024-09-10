from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_email
from base.models import *
from Products.PhotoResize import compress_image, save_image


class Profile(BaseModel):
    user = models.OneToOneField( User, on_delete=models.CASCADE , related_name="profile")
    is_email_valid = models.BooleanField()
    email_token = models.CharField( max_length=100, null=True  , blank= True )
    user_image = models.ImageField(upload_to="profile",null=True  , blank= True )
    
    

    

class UsersDetail(models.Model):
    Name = models.TextField(max_length= 100)
    email = models.EmailField(validators=[validate_email],default='default@example.com')
    first_name = models.TextField(max_length= 100, default='Anonymous')
    last_name= models.TextField(max_length= 100, default='Anonymous') 
    start_date = models.DateField() 
    
    def __str__(self):
        return self.Name

# class UsersDetail(models.Model):
#     Name = models.TextField(max_length= 100)
#     email = models.EmailField(validators=[validate_email],default='default@example.com')
#     Gender = models.CharField(max_length=2)
#     Birthtown = models.TextField()
#     birth_date = models.CharField(max_length=255)
#     Street = models.TextField()
#     start_date = models.DateField()
    
    
    

#     def __str__(self):
#         return self.Name
    
# class PasswordReset(models.Model):
#     user = models.OneToOneField(User , on_delete=models.CASCADE)
#     forgot_password_token = models.CharField(max_length= 100)
#     created_at= models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.user.username

