# Generated by Django 3.0.7 on 2020-07-06 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cplus', '0026_auto_20200705_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='fecha',
        ),
    ]
