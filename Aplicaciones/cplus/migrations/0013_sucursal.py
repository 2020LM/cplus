# Generated by Django 3.0.7 on 2020-06-29 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cplus', '0012_producto_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=500)),
            ],
        ),
    ]
