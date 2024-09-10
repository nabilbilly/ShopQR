from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def compress_image(uploaded_image):
    img = Image.open(uploaded_image)
    img = img.convert("RGB")
    img.thumbnail((800, 800))  # Resize to max dimensions
    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=85)
    return ContentFile(buffer.getvalue(), uploaded_image.name)

def save_image(instance, *args, **kwargs):
    instance.image = compress_image(instance.image)
    instance.__class__.base_class.save(instance, *args, **kwargs)
