# Generated by Django 2.0.8 on 2018-08-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarManagment', '0006_auto_20180822_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=30),
        ),
    ]
