# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-21 02:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('docstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 4, 21, 2, 20, 18, 605164, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2018, 4, 21, 2, 20, 29, 869106, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
