# Generated by Django 4.2.1 on 2023-05-16 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_discription_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone_no',
            field=models.PositiveIntegerField(default=0, max_length=10),
        ),
    ]
