# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-28 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0002_auto_20180428_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='additional_info',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='guest',
            name='contact_info',
            field=models.CharField(blank=True, default='', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='food_type',
            field=models.CharField(choices=[('Standardowe', 'Standardowe'), ('Wegetarianskie', 'Wegetarianskie'), ('Weganskie', 'Weganskie')], max_length=15),
        ),
        migrations.AlterField(
            model_name='guest',
            name='night_stay',
            field=models.CharField(choices=[('Nie chc\u0119 pokoju', 'Nie chc\u0119 pokoju'), ('2-osobowy standard', '2-osobowy standard'), ('1-osobowy standard', '1-osobowy standard'), ('2-osobowy deluxe', '2-osobowy deluxe'), ('1-osobowy deluxe', '1-osobowy deluxe'), ('Apartament', 'Apartament')], max_length=18),
        ),
        migrations.AlterField(
            model_name='guest',
            name='transport',
            field=models.CharField(choices=[('Nie potrzeba', 'Nie potrzeba'), ('Spod ko\u015bcio\u0142a do hotelu', 'Spod ko\u015bcio\u0142a do hotelu'), ('Z placu przed kolegiat\u0105 Przemienienia Pa\u0144skiego w Radzyminie', 'Z placu przed kolegiat\u0105 Przemienienia Pa\u0144skiego w Radzyminie'), ('Z Dworca Wile\u0144skiego w Warszawie', 'Z Dworca Wile\u0144skiego w Warszawie')], max_length=60),
        ),
    ]
