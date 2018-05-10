# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict

from django.db.models import Count
from django.shortcuts import render
from django.utils.timezone import now
from django.views import View

from guests.forms import Password_Form, Confirm_Form, Guest_Filter_Form
from guests.models import Guest, Information_Broadcast


class Guests_Management(View):
    template_name = 'guest_management.html'
    title = "Guest management"
    not_selected = "NIE WYBRANO"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      {"title": self.title,
                       "guest_list": Guest.objects.all(),
                       "statistics": self._statistics(),
                       "confirmed": self._calculate_confirmed_stats(),
                       "filter_form": Guest_Filter_Form()
                       })

    def _statistics(self):
        statistics = {}
        self._calculate_stat(statistics, "transport")
        self._calculate_stat(statistics, "night_stay")
        self._calculate_stat(statistics, "food_type")
        self._calculate_stat(statistics, "confirm")
        self._calculate_stat(statistics, "invitation_given")
        return statistics

    def _calculate_stat(self, statistics, stat_name):
        stat = {self.not_selected: 0}
        for each in Guest.objects.values(stat_name).annotate(Count(stat_name)):
            key = each[stat_name]
            val = each[stat_name + "__count"]
            stat[key] = val
        for each in [None, '', False, 'false', 'None']:
            if stat.get(each):
                stat[self.not_selected] += stat[each]
                del stat[each]
        statistics[stat_name.capitalize().replace("_", " ")] = stat

    def _calculate_confirmed_stats(self):
        confirmed = OrderedDict()
        confirmed["Hers"] = [0, 0, 0, 0]
        confirmed["His"] = [0, 0, 0, 0]
        confirmed["Both"] = [0, 0, 0, 0]
        confirmed["Sum"] = [0, 0, 0, 0]
        for guest in Guest.objects.all():
            confirmed[guest.side][0] += guest.confirmed_adults
            confirmed[guest.side][1] += guest.confirmed_children
            confirmed[guest.side][2] += guest.confirmed_toddlers
            confirmed[guest.side][3] += sum((guest.confirmed_adults, guest.confirmed_children, guest.confirmed_toddlers))
        for side in ("His", "Hers", "Both"):
            for i in range(4):
                confirmed["Sum"][i] += confirmed[side][i]
        return confirmed


class Guest_Confirm(View):
    title = "Potwierdzenie przybycia"

    def get(self, request, *args, **kwargs):
        form = Password_Form()
        return render(request, "guest_password.html",
                      {"title": self.title,
                       "form": form})

    def post(self, request, *args, **kwargs):
        if request.POST.get("step") == '1':
            return self._handle_step_1(request)
        else:
            return self._handle_step_2(request)

    def _handle_step_1(self, request):
        password_form = Password_Form(data=request.POST)
        if password_form.is_valid():
            form = Confirm_Form(instance=password_form.found_guest)
            return self._render_confirm_form(request, form)
        else:
            return render(request, "guest_password.html",
                          {"title": self.title,
                           "form": password_form})

    def _handle_step_2(self, request):
        form = Confirm_Form(instance=Guest.objects.get(password=request.POST.get("password")),
                            data=request.POST)
        if form.is_valid():
            form.instance.confirmation_date = now()
            form.instance.invitation_given = True
            form.save()
            return render(request, 'main.html',
                          {"title": "Dziekujemy za potwierdzenie!"})
        else:
            return self._render_confirm_form(request, form)

    def _render_confirm_form(self, request, form):
        return render(request, 'guest_confirm.html',
                      {"title": self.title,
                       "form": form,
                       "guest_information": Information_Broadcast.objects.all()})
