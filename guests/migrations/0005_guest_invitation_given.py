# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-01 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0004_auto_20180430_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='invitation_given',
            field=models.BooleanField(default=False),
        ),
    ]
