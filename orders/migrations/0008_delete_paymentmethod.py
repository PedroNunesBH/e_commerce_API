# Generated by Django 5.0.1 on 2024-02-02 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_payment_method'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentMethod',
        ),
    ]