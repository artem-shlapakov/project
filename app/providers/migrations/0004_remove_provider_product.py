# Generated by Django 4.0.6 on 2022-08-02 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0003_provider_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='product',
        ),
    ]
