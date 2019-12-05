from django.forms import ModelForm, Textarea, DateInput
from . import models
from setups import models as s_models


class ProjectCreateForm(ModelForm):
    class Meta:
        model = models.Project
        fields = ['name', 'type', 'start_date', 'region', 'district', 'town', 'duration', 'authority', 'consultant', 'quantity_demanded', 'quantity_supplied', 'remarks']
        widgets = {
            'remarks': Textarea(attrs={'rows': 2}),
            'start_date': DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # if self.instance.region:
        #     self.fields['district'].queryset = s_models.District.objects.filter(region=self.instance.region)
        # else:
        #     self.fields['district'].queryset = s_models.District.objects.none()


class ProjectUpdateForm(ModelForm):
    class Meta:
        model = models.Project
        fields = ['name', 'type', 'start_date', 'status', 'region', 'district', 'town', 'duration', 'authority', 'consultant', 'quantity_demanded', 'quantity_supplied', 'remarks']
        widgets = {
            'remarks': Textarea(attrs={'rows': 2}),
            'start_date': DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # if self.instance.region:
        #     self.fields['district'].queryset = s_models.District.objects.filter(region=self.instance.region)
        # else:
        #     self.fields['district'].queryset = s_models.District.objects.none()
