# Generated by Django 3.2.6 on 2023-05-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0009_alter_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=13),
        ),
    ]
