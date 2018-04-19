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


Confirm_Form = forms.modelform_factory(
    Guest,
    fields=("confirmed_adults",
            "confirmed_children",
            "confirmed_toddlers",
            "transport",
            "night_stay",
            "food_type",
            "password",
            "confirm"),
    widgets={"confirm": forms.Select(choices=(("", "---------"),
                                              (True, "Tak"),
                                              ( False, "Nie"))),
             "confirmation_date": forms.HiddenInput,
             "password": forms.HiddenInput}
)


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
