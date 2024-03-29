# Generated by Django 5.0.1 on 2024-02-01 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.FloatField()),
                ('address_to_delivery', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_order', to='clients.client')),
                ('products', models.ManyToManyField(related_name='products_order', to='products.product')),
            ],
        ),
    ]
