from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from bootstrap_datepicker_plus import DatePickerInput

from .models import Event


class EventHostForm(forms.ModelForm):
    email = forms.EmailField(label=_("E-mail address"))

    def clean_start(self):
        start = self.cleaned_data["start"]
        if start < timezone.now():
            raise forms.ValidationError(_("Has to be in the future"))
        return start

    class Meta:
        fields = ["start", "email"]
        model = Event

        widgets = {
            'start': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }


class JoinForm(forms.Form):
    email = forms.EmailField(label=_("E-mail address"))

    class Meta:
        fields = ["email"]
        
        widgets = {
            'start': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }

