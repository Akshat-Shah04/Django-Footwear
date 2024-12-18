# Generated by Django 5.1 on 2024-11-23 13:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0013_remove_cart_total_alter_cart_time_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='roundtotal',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cart',
            name='time_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='ttime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]