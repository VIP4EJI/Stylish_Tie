# Generated by Django 3.1.7 on 2021-04-13 02:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210412_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 2, 21, 53, 334107)),
        ),
    ]
