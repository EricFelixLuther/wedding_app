# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Labels(models.Model):
    label = models.CharField(max_length=24)

    def __unicode__(self):
        return self.label


class Guest(models.Model):
    name = models.CharField(max_length=128)
    nickname = models.CharField(max_length=32, blank=True, null=True, default='')
    side = models.CharField(max_length=4, choices=(("His", "His"), ("Hers", "Hers"), ("Both", "Both")))
    labels = models.ManyToManyField(Labels, blank=True)
    priority = models.CharField(max_length=10, choices=(("High", "High"), ("Medium", "Medium"), ("Low", "Low")))
    confirmed_adults = models.PositiveSmallIntegerField(default=0)
    confirmed_children = models.PositiveSmallIntegerField(default=0)
    confirmed_toddlers = models.PositiveSmallIntegerField(default=0)
    password = models.CharField(max_length=10, unique=True)
    transport = models.BooleanField(default=False)
    night_stay = models.BooleanField(default=False)
    food_type = models.CharField(max_length=15, default="Standardowe", choices=(("Standardowe", "Standardowe"),
                                                                                ("Wegetarianskie", "Wegetarianskie"),
                                                                                ("Weganskie", "Weganskie")))
    confirm = models.NullBooleanField(default=None)

    def __unicode__(self):
        return self.name