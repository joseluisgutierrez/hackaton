# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='padre',
            old_name='hijos',
            new_name='Shijos',
        ),
    ]
