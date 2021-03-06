# Generated by Django 2.0.8 on 2018-08-22 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CarManagment', '0003_auto_20180822_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarManagment.Car')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarManagment.Service')),
            ],
        ),
        migrations.RemoveField(
            model_name='mileagehistory',
            name='car',
        ),
        migrations.DeleteModel(
            name='MileageHistory',
        ),
    ]
