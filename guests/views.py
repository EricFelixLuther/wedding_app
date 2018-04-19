# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.shortcuts import render
from django.views import View

from guests.models import Guest


class Guests_Management(View):
    template_name = 'guest_management.html'
    title = "Guest management"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      {"title": self.title,
                       "formset": forms.modelformset_factory(Guest, fields="__all__")})

    def post(self, request, *args, **kwargs):
        raw_formset = forms.modelformset_factory(Guest, fields="__all__")
        formset = raw_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            formset = raw_formset()
        return render(request, self.template_name,
                      {"title": self.title,
                       "formset": formset})


class Guest_Confirm(View):
    template_name = 'guest_confirm.html'
    title = "Potwierdzenie przybycia"

    def get(self, request, *args, **kwargs):
        form = forms.modelform_factory(Guest, fields=("password"))()
        return render(request, self.template_name,
                      {"title": self.title,
                       "form": form})

    def post(self, request, *args, **kwargs):
        guest = Guest.objects.get(password=request.POST.get("password"))
        raw_form = forms.modelform_factory(Guest,
                                           fields=("confirmed_adults", "confirmed_children", "confirmed_toddlers",
                                                   "transport", "night_stay", "food_type", "password", "confirm"))
        form = raw_form(instance=guest)
        return render(request, self.template_name,
                      {"title": self.title,
                       "form": form})
