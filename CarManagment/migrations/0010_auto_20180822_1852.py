# Generated by Django 2.0.8 on 2018-08-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarManagment', '0009_auto_20180822_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='product_year',
            field=models.PositiveIntegerField(),
        ),
    ]
