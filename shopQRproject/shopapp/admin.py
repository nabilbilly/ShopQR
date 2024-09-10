from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib import admin


@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('data', 'image')  # Adjust the fields as needed
    search_fields = ('data',)        # Enable search functionality based on the 'data' field
    model = QRCode

