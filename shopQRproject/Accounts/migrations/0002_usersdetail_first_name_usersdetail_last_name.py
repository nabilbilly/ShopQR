# Generated by Django 5.0.7 on 2024-08-10 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersdetail',
            name='first_name',
            field=models.TextField(default='Anonymous', max_length=100),
        ),
        migrations.AddField(
            model_name='usersdetail',
            name='last_name',
            field=models.TextField(default='Anonymous', max_length=100),
        ),
    ]
