# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ranks', '0003_player_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='buy_in_amount',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='rank',
            field=models.IntegerField(default=9999),
            preserve_default=True,
        ),
    ]
