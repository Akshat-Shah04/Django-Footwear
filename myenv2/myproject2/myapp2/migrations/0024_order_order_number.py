# Generated by Django 5.1 on 2024-12-18 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0023_rename_phone_number_billing_mobile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.BigIntegerField(default=1000, unique=True),
        ),
    ]