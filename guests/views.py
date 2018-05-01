# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils.timezone import now
from django.views import View

from guests.forms import Password_Form, Confirm_Form
from guests.models import Guest


class Guests_Management(View):
    template_name = 'guest_management.html'
    title = "Guest management"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      {"title": self.title,
                       "guest_list": Guest.objects.all()})


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
            form.save()
            return render(request, 'main.html',
                          {"title": "Dziekujemy za potwierdzenie!"})
        else:
            return self._render_confirm_form(request, form)

    def _render_confirm_form(self, request, form):
        return render(request, 'guest_confirm.html',
                      {"title": self.title,
                       "form": form})
