# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magicsite', '0002_auto_20180522_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='score',
        ),
        migrations.AddField(
            model_name='option',
            name='op_type',
            field=models.CharField(default='', max_length=1),
        ),
    ]
