# Generated by Django 2.0.8 on 2018-08-22 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CarManagment', '0007_auto_20180822_1758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicehistory',
            options={'ordering': ('current_mileage',), 'verbose_name_plural': 'Service histories'},
        ),
    ]
