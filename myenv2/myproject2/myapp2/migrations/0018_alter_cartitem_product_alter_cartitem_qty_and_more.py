# Generated by Django 5.1 on 2024-12-14 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0017_rename_cartitems_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='myapp2.product'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='qty',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount_value',
            field=models.IntegerField(),
        ),
    ]