from django.db import models

class QRCode(models.Model):
    data = models.CharField(max_length=255)
    image = models.ImageField(upload_to='qr_codes/')
    
    def __str__(self):
        return self.data

