# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piserver', '0002_choice_off'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='off',
            field=models.IntegerField(default=1),
        ),
    ]
