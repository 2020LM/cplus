# Generated by Django 3.0.7 on 2020-07-05 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cplus', '0023_funcion2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcion',
            name='fecha',
            field=models.DateField(max_length=500),
        ),
        migrations.AlterField(
            model_name='funcion',
            name='hora',
            field=models.TimeField(max_length=500),
        ),
    ]
