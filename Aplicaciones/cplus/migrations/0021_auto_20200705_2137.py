# Generated by Django 3.0.7 on 2020-07-05 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cplus', '0020_auto_20200705_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcion',
            name='Sala',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cplus.Sala'),
        ),
        migrations.AddField(
            model_name='funcion',
            name='fecha',
            field=models.CharField(default='Hola', max_length=500),
        ),
        migrations.AddField(
            model_name='funcion',
            name='hora',
            field=models.CharField(default='Hola', max_length=500),
        ),
        migrations.AddField(
            model_name='funcion',
            name='pelicula',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cplus.Pelicula'),
        ),
        migrations.AddField(
            model_name='funcion',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cplus.Sucursal'),
        ),
    ]