# Generated by Django 3.1.7 on 2021-04-18 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210417_0027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('title',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]