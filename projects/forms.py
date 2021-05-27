from django import forms
from . import models
from setups import models as s_models


class ProjectCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectCreateForm, self).__init__(*args, **kwargs)
        # self.fields['price'].label = "Price/t (TZS)"
        # self.fields['authority'].label = "Client"

    class Meta:
        model = models.Project
        fields = ['name', 'client', 'type', 'size', 'start_date', 'region', 'district', 'town', 'duration', 'quantity_demanded', 'quantity_supplied', 'remarks', 'latitude', 'longitude']
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 2}),
            'start_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'price': forms.NumberInput(),
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['name', 'client', 'type', 'size', 'start_date', 'status', 'region', 'district', 'town', 'duration', 'quantity_demanded', 'quantity_supplied', 'remarks', 'latitude', 'longitude']
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
