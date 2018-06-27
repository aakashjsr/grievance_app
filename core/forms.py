from django import forms
from core.models import Case
from django.contrib.admin.widgets import AdminDateWidget

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        exclude = ("incident_phase",)
        widgets = {
            "incident_date": forms.SelectDateWidget
        }

    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields["incident_date"].widget.attrs.update({"class": "custom-date form-control"})
