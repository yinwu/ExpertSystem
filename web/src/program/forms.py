from django import forms
from .models import Program


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = {
            "seq",
            "name",
            "desp",
            "responser",
            "location",
            "money"
        }

    create_time = forms.DateField(label="项目创建时间")
    start_time = forms.DateField(label="招标开始时间")
    finish_time = forms.DateField(label="招标结束时间")