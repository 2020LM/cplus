# Generated by Django 3.0.7 on 2020-07-07 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cplus', '0027_remove_entrada_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto_VIP',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=500)),
                ('nombre', models.CharField(max_length=500)),
                ('descripcion', models.CharField(max_length=2000)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cplus.Cliente')),
            ],
        ),
    ]
