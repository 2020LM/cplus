# Generated by Django 3.0.7 on 2020-07-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cplus', '0021_auto_20200705_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcion',
            name='fecha',
            field=models.DateField(default='Hola', max_length=500),
        ),
        migrations.AlterField(
            model_name='funcion',
            name='hora',
            field=models.TimeField(default='Hola', max_length=500),
        ),
    ]
