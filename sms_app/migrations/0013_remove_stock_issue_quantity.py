# Generated by Django 3.2.4 on 2021-06-05 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0012_remove_stock_quantity_before'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='issue_quantity',
        ),
    ]
