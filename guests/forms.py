import random
import string

from django import forms

from guests.models import Guest, Labels


class Password_Form(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ["password"]

    def clean(self):
        try:
            self.found_guest = self.Meta.model.objects.get(password=self.cleaned_data["password"])
        except self.Meta.model.DoesNotExist:
            self.found_guest = None
            self.add_error("password", "Nie rozpoznano hasla.")
        return self.cleaned_data


class Confirm_Form(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ("confirmed_adults",
                  "confirmed_children",
                  "confirmed_toddlers",
                  "transport",
                  "night_stay",
                  "food_type",
                  "password",
                  "confirm",
                  "additional_info",
                  "contact_info")
        widgets = {"confirm": forms.Select(choices=(("on", "Tak"),
                                                    ('', "Nie"))),
                   "confirmation_date": forms.HiddenInput,
                   "password": forms.HiddenInput}

    def clean(self):
        if self.cleaned_data["confirm"]:
            for field in ("transport", "night_stay", "food_type"):
                if not self.cleaned_data[field]:
                    self.add_error(field, "To pole jest wymagane")
        else:
            self.cleaned_data["confirmed_adults"] = 0
            self.cleaned_data["confirmed_children"] = 0
            self.cleaned_data["confirmed_toddlers"] = 0
            self.cleaned_data["transport"] = ''
            self.cleaned_data["night_stay"] = ''
            self.cleaned_data["food_type"] = ''
        return self.cleaned_data


class Guest_Filter_Form(forms.ModelForm):
    class Meta:
        model = Guest
        fields = "__all__"
        widgets = {"side": forms.Select(choices=(("His", "His"), ("Hers", "Hers"), ("Both", "Both"))),
                   "labels": forms.Select(choices=((label.label, label.label) for label in Labels.objects.all())),
                   "priority": forms.Select(choices=(("High", "High"), ("Medium", "Medium"), ("Low", "Low"))),
                   "confirm": forms.Select(choices=(("", "Wszystkie"), ("None", "Nie otwarto"), ("False", "Nie potwierdzono"), ("True", "Potwierdzono"))),
                   "confirmation_date": forms.Select(choices=(("", "Wszystkie"), ("None", "Brak daty"))),
                   "invitation_given": forms.Select(choices=(("", "Wszystkie"), ("True", "Wydane"), ("False", "Nie wydane"))),
                   "additional_info": forms.TextInput}
