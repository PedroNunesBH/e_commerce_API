# Generated by Django 5.0.1 on 2024-02-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='each_product_quantity',
            field=models.JSONField(default=[1]),
        ),
    ]
