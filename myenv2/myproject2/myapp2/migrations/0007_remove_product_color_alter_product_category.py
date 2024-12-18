# Generated by Django 5.1 on 2024-10-28 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0006_alter_user_profile_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('running', 'Running'), ('casual', 'Casual'), ('formal', 'Formal'), ('sports', 'Sports'), ('sneakers', 'Sneakers')], max_length=50),
        ),
    ]
