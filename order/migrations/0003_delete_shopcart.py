# Generated by Django 3.1 on 2020-08-23 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200823_1947'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShopCart',
        ),
    ]