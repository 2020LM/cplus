# Generated by Django 3.0.7 on 2020-06-28 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cplus', '0007_producto_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.CharField(max_length=500)),
                ('hora', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('AsientosDisponibles', models.IntegerField()),
                ('AsientosOcupados', models.IntegerField()),
                ('NumeroDeAsientos', models.IntegerField()),
            ],
        ),
    ]
