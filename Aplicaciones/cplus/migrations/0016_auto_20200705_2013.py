# Generated by Django 3.0.7 on 2020-07-05 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cplus', '0015_sala_sucursal'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcion',
            name='Sala',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cplus.Sala'),
        ),
        migrations.AddField(
            model_name='funcion',
            name='pelicula',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cplus.Pelicula'),
        ),
    ]
