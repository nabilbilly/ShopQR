# Generated by Django 5.0.7 on 2024-08-10 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_usersdetail_first_name_usersdetail_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersdetail',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='usersdetail',
            name='last_name',
        ),
    ]
