# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ranks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='earnings',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
