from django import forms
from .models import Expert

class ExpertForm(forms.ModelForm):
    class Meta:
        model = Expert
        fields = {"name", "phone", "email", "address", "unit", "degree", "level", "program_type"}