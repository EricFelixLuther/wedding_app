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
    confirmed_adults = models.PositiveSmallIntegerField(default=0, blank=True)
    confirmed_children = models.PositiveSmallIntegerField(default=0, blank=True)
    confirmed_toddlers = models.PositiveSmallIntegerField(default=0, blank=True)
    password = models.CharField(max_length=10, unique=True, blank=True)
    transport = models.CharField(max_length=60, blank=True, null=True, default='', choices=(
        ("Nie potrzeba", "Nie potrzeba"),
        ("Spod kościoła do hotelu", "Spod kościoła do hotelu"),
        ("Z placu przed kolegiatą Przemienienia Pańskiego w Radzyminie",
         "Z placu przed kolegiatą Przemienienia Pańskiego w Radzyminie"),
        ("Z Dworca Wileńskiego w Warszawie", "Z Dworca Wileńskiego w Warszawie")
    ))
    night_stay = models.CharField(max_length=18, blank=True, null=True, default='', choices=(
        ("Nie chcę pokoju", "Nie chcę pokoju"),
        ("2-osobowy standard", "2-osobowy standard"),
        ("1-osobowy standard", "1-osobowy standard"),
        ("2-osobowy deluxe", "2-osobowy deluxe"),
        ("1-osobowy deluxe", "1-osobowy deluxe"),
        ("Apartament", "Apartament")
    ))
    food_type = models.CharField(max_length=15, blank=True, null=True, default='',
                                 choices=(("Standardowe", "Standardowe"),
                                          ("Wegetarianskie", "Wegetarianskie"),
                                          ("Weganskie", "Weganskie")))
    confirm = models.NullBooleanField(default=None)
    confirmation_date = models.DateTimeField(blank=True, null=True, default=None)
    contact_info = models.CharField(max_length=64, blank=True, null=True, default='')
    additional_info = models.TextField(blank=True, null=True, default='')
    invitation_given = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def format_labels(self):
        return ", ".join(list(self.labels.values_list("label", flat=True)))
