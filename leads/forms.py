from django import forms
from .models import Lead, Lead

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "first_name", "last_name", "age", "agent"
        )

class LeadForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    age = forms.IntegerField(min_value=0)

