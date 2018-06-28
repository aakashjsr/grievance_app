from django import forms
from core.models import Case, ResponsibleEntity


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        exclude = ("incident_phase",)

    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields["incident_date"].widget.attrs.update({"class": "custom-date form-control datepicker"})
        self.fields["incident_date"].widget.attrs.update({"placeholder": "Select date"})


class ResponsibilityForm(forms.ModelForm):
    class Meta:
        model = ResponsibleEntity
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ResponsibilityForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})