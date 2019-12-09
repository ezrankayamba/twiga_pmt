
import django_filters as filters
from . import models
from setups import models as s_models


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains', label="Name")
    contractors__contractor = filters.ModelChoiceFilter(queryset=s_models.Contractor.objects.all(), label="Contractor")
    suppliers__supplier = filters.ModelChoiceFilter(queryset=s_models.Supplier.objects.all(), label="Supplier")
    consultants__consultant = filters.ModelChoiceFilter(queryset=s_models.Consultant.objects.all(), label="Consultant")
    financers__financer = filters.ModelChoiceFilter(queryset=s_models.Financer.objects.all(), label="Financer")

    class Meta:
        model = models.Project
        fields = ['name', 'type', 'size', 'status', 'region', 'district', 'authority', 'financers__financer', 'contractors__contractor', 'suppliers__supplier', 'consultants__consultant']
