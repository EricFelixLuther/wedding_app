# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-19 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('nickname', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('side', models.CharField(choices=[('His', 'His'), ('Hers', 'Hers'), ('Both', 'Both')], max_length=4)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=10)),
                ('confirmed_adults', models.PositiveSmallIntegerField(default=0)),
                ('confirmed_children', models.PositiveSmallIntegerField(default=0)),
                ('confirmed_toddlers', models.PositiveSmallIntegerField(default=0)),
                ('password', models.CharField(max_length=10, unique=True)),
                ('transport', models.BooleanField(default=False)),
                ('night_stay', models.BooleanField(default=False)),
                ('food_type', models.CharField(choices=[('Standardowe', 'Standardowe'), ('Wegetarianskie', 'Wegetarianskie'), ('Weganskie', 'Weganskie')], default='Standardowe', max_length=15)),
                ('confirm', models.NullBooleanField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=24)),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='labels',
            field=models.ManyToManyField(blank=True, to='guests.Labels'),
        ),
    ]
