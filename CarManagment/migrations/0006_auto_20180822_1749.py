# Generated by Django 2.0.8 on 2018-08-22 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarManagment', '0005_auto_20180822_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicehistory',
            name='current_mileage',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicehistory',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]