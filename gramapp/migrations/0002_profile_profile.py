# Generated by Django 3.0.8 on 2020-07-08 08:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gramapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Profile',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]