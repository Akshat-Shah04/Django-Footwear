# Generated by Django 5.1 on 2024-11-21 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0012_alter_cart_time_date_alter_wishlist_ttime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
        migrations.AlterField(
            model_name='cart',
            name='time_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 21, 10, 35, 20, 745078, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='ttime',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 21, 10, 35, 20, 745078, tzinfo=datetime.timezone.utc)),
        ),
    ]
