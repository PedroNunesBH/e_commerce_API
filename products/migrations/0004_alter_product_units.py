# Generated by Django 5.0.1 on 2024-02-01 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='units',
            field=models.PositiveIntegerField(),
        ),
    ]