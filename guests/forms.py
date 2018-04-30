import random
import string

from django import forms

from guests.models import Guest


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
        print self.cleaned_data
        if self.cleaned_data["confirm"]:
            print "here"
            for field in ("transport", "night_stay", "food_type"):
                if not self.cleaned_data[field]:
                    self.add_error(field, "To pole jest wymagane")
        else:
            print "here 2"
            self.cleaned_data["confirmed_adults"] = 0
            self.cleaned_data["confirmed_children"] = 0
            self.cleaned_data["confirmed_toddlers"] = 0
            self.cleaned_data["transport"] = ''
            self.cleaned_data["night_stay"] = ''
            self.cleaned_data["food_type"] = ''
        return self.cleaned_data


pwd_characters = string.letters + string.digits


class Guest_Form(forms.ModelForm):
    class Meta:
        model = Guest
        fields = "__all__"

    def clean(self):
        if not self.cleaned_data["password"]:
            self.cleaned_data["password"] = self._generate_password()
        return self.cleaned_data

    def _generate_password(self):
        pwd = ''
        for i in range(10):
            pwd += random.choice(pwd_characters)
        return pwd


Guest_Formset = forms.modelformset_factory(Guest, form=Guest_Form)
