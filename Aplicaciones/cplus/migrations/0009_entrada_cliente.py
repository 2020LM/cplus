# Generated by Django 3.0.7 on 2020-06-28 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cplus', '0008_funcion_sala'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cplus.Cliente'),
        ),
    ]
