# Generated by Django 2.0.5 on 2018-08-06 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_auto_20180516_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.CharField(default=datetime.datetime(2018, 8, 6, 16, 28, 52, 554433), max_length=200),
        ),
        migrations.AlterField(
            model_name='file',
            name='time',
            field=models.CharField(default=datetime.datetime(2018, 8, 6, 16, 28, 52, 553458), max_length=200),
        ),
    ]