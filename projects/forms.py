from django import forms
from . import models
from setups import models as s_models


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['name', 'type', 'size', 'start_date', 'region', 'district', 'town', 'duration', 'authority', 'quantity_demanded', 'quantity_supplied', 'remarks', 'latitude', 'longitude']
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 2}),
            'start_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['name', 'type', 'size', 'start_date', 'status', 'region', 'district', 'town', 'duration', 'authority', 'quantity_demanded', 'quantity_supplied', 'remarks', 'latitude', 'longitude']
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 2}),
            'start_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }


class ProjectAuditCreateForm(forms.ModelForm):
    class Meta:
        model = models.ProjectAudit
        fields = ['remarks']
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 3}),
        }


class UploadFileForm(forms.Form):
    file = forms.FileField()
