# Generated by Django 4.2.1 on 2023-05-17 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers', '0005_remove_category_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
