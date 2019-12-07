
import django_filters
from . import models


class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Project
        fields = ['name', 'type', 'status']
