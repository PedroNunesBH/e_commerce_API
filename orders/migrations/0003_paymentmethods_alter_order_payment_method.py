# Generated by Django 5.0.1 on 2024-02-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_payment_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.IntegerField(default=1, max_length=50),
        ),
    ]
