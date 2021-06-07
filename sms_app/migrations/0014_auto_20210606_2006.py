# Generated by Django 3.2.4 on 2021-06-06 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0013_remove_stock_issue_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='category',
            field=models.CharField(blank=True, choices=[('Furniture', 'Furniture'), ('Sport', 'Sport'), ('Accessories Auto', 'Accessories Auto'), ('Movies', 'Movies')], max_length=40, null=True, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
