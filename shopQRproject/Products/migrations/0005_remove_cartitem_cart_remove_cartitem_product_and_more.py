# Generated by Django 5.0.7 on 2024-09-05 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_remove_cartitem_color_variant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
