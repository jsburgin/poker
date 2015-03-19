# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_id', models.IntegerField(default=-1)),
                ('second_id', models.IntegerField(default=-1)),
                ('third_id', models.IntegerField(default=-1)),
                ('fourth_id', models.IntegerField(default=-1)),
                ('first_earnings', models.FloatField(default=0.0)),
                ('second_earnings', models.FloatField(default=0.0)),
                ('third_earnings', models.FloatField(default=0.0)),
                ('fourth_earnings', models.FloatField(default=0.0)),
                ('date_played', models.DateTimeField(verbose_name=b'Date Played')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('first_places', models.IntegerField(default=0)),
                ('second_places', models.IntegerField(default=0)),
                ('third_places', models.IntegerField(default=0)),
                ('fourth_places', models.IntegerField(default=0)),
                ('total_games_played', models.IntegerField(default=0)),
                ('rank', models.IntegerField(default=-9999)),
                ('games_played_in', models.ManyToManyField(to='ranks.Game')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'series',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='series',
            field=models.ForeignKey(to='ranks.Series'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='series',
            field=models.ForeignKey(to='ranks.Series'),
            preserve_default=True,
        ),
    ]
