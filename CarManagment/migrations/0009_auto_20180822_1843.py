# Generated by Django 2.0.8 on 2018-08-22 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarManagment', '0008_auto_20180822_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='product_date',
        ),
        migrations.AddField(
            model_name='car',
            name='product_year',
            field=models.PositiveIntegerField(default=2000, max_length=4),
            preserve_default=False,
        ),
    ]
