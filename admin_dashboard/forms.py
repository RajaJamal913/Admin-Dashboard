from django import forms
from .models import PanelRate

class PanelRateForm(forms.ModelForm):
    class Meta:
        model = PanelRate
        fields = ['rate']
