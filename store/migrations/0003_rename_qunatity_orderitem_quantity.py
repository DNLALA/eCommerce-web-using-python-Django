# Generated by Django 4.0.6 on 2022-07-25 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]
