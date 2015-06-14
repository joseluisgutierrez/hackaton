# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0002_auto_20150614_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='padre',
            name='Shijos',
        ),
        migrations.AddField(
            model_name='padre',
            name='Shijos',
            field=models.ForeignKey(related_name='Shijos', default=1, to='apprest.Hijo'),
            preserve_default=False,
        ),
    ]
