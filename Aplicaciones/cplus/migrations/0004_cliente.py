# Generated by Django 3.0.7 on 2020-06-28 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cplus', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=500)),
                ('apellido', models.CharField(max_length=500)),
                ('monedasVIP', models.IntegerField()),
            ],
        ),
    ]
