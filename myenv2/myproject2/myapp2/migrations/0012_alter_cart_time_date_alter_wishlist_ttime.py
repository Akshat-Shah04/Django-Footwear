# Generated by Django 5.1 on 2024-11-21 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0011_alter_cart_time_date_alter_wishlist_ttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='time_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 21, 10, 9, 33, 527959, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='ttime',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 21, 10, 9, 33, 526955, tzinfo=datetime.timezone.utc)),
        ),
    ]
