from django import forms
from .models import Pateint


class PatientForm(forms.ModelForm):
    class Meta:
        model = Pateint
        fields = ('full_name', 'email', 'mobile_no', 'address',
                  'detail', 'precount', 'next_visit_date', )
