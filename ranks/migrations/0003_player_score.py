# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ranks', '0002_player_earnings'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='score',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
