# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 13:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tester',
            name='parent',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tester',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 12, 14, 25, 33, 735472)),
        ),
    ]