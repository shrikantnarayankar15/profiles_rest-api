# Generated by Django 2.2.6 on 2019-10-31 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='product_img_field',
            field=models.ImageField(max_length=254, upload_to='media'),
        ),
    ]
