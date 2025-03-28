# Generated by Django 5.1 on 2024-12-14 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0015_coupon_remove_cart_roundtotal_cart_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='qty',
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='myapp2.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp2.product')),
            ],
        ),
    ]
