from django.forms import ModelForm, Textarea, DateInput, HiddenInput
from . import models
from setups import models as s_models


class ProjectCreateForm(ModelForm):
    class Meta:
        model = models.Project
        fields = ['name', 'type', 'size', 'start_date', 'region', 'district', 'town', 'duration', 'authority', 'quantity_demanded', 'quantity_supplied', 'remarks', 'latitude', 'longitude']
        widgets = {
            'remarks': Textarea(attrs={'rows': 2}),
            'start_date': DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'latitude': HiddenInput(),
            'longitude': HiddenInput(),
        }


class ProjectUpdateForm(ModelForm):
    class Meta:
        model = models.Project
        fields = ['name', 'type', 'size', 'start_date', 'status', 'region', 'district', 'town', 'duration', 'authority', 'quantity_demanded', 'quantity_supplied', 'remarks', 'latitude', 'longitude']
        widgets = {
            'remarks': Textarea(attrs={'rows': 2}),
            'start_date': DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'latitude': HiddenInput(),
            'longitude': HiddenInput(),
        }


class ProjectAuditCreateForm(ModelForm):
    class Meta:
        model = models.ProjectAudit
        fields = ['remarks']
        widgets = {
            'remarks': Textarea(attrs={'rows': 3}),
        }
