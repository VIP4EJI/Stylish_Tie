# Generated by Django 3.1.7 on 2021-04-16 01:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20210413_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 16, 1, 23, 34, 891562)),
        ),
    ]
