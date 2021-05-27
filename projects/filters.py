
import django_filters as filters
from . import models
from setups import models as s_models


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains', label="Name")
    contractors__contractor = filters.ModelChoiceFilter(queryset=s_models.Contractor.objects.all(), label="Contractor")
    suppliers__supplier = filters.ModelChoiceFilter(queryset=s_models.Supplier.objects.all(), label="Supplier")
    suppliers__brand = filters.ModelChoiceFilter(queryset=s_models.Brand.objects.all(), label="Brand")
    consultants__consultant = filters.ModelChoiceFilter(queryset=s_models.Consultant.objects.all(), label="Consultant")
    financers__financer = filters.ModelChoiceFilter(queryset=s_models.Financer.objects.all(), label="Financer")
    authority = filters.ModelChoiceFilter(queryset=s_models.Authority.objects.all(), label="Client")

    class Meta:
        model = models.Project
        fields = ['name', 'type', 'size', 'status', 'region', 'district', 'suppliers__brand', 'financers__financer', 'suppliers__supplier', 'contractors__contractor', 'consultants__consultant']
