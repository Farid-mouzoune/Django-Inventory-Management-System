# Generated by Django 3.2.4 on 2021-06-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0006_alter_stock_tags_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='total_quantity',
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Unit Price'),
        ),
    ]