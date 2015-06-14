# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hijo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.CharField(unique=True, max_length=8)),
                ('genero', models.CharField(max_length=5)),
                ('direccion', models.CharField(max_length=200)),
                ('fechaNaci', models.DateField(verbose_name=b'Fecha de nacimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Padre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('dni', models.CharField(unique=True, max_length=8)),
                ('hijos', models.ManyToManyField(to='apprest.Hijo')),
            ],
        ),
    ]
