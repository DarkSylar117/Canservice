# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionalidad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
