# Generated by Django 2.0.8 on 2018-08-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarManagment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('period', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='mileage',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mileagehistory',
            name='mileage',
            field=models.PositiveIntegerField(),
        ),
    ]