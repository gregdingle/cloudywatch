from django import forms

from .models import Application


class FindToolForm(forms.Form):
    application = forms.ModelChoiceField(queryset=Application.objects.enabled(), empty_label=None)
