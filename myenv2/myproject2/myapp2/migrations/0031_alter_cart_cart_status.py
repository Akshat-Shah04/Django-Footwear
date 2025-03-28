# Generated by Django 5.1 on 2024-12-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0030_alter_order_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_status',
            field=models.CharField(choices=[('Active', 'Active'), ('Cancelled', 'Cancelled'), ('Delivered', 'Delivered'), ('Shipping', 'Shipping'), ('Ordered', 'Ordered'), ('Paid', 'Paid'), ('Saved', 'Saved')], default='Active', max_length=20),
        ),
    ]
