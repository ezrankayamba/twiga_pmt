from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from projects import models as prj_models
from django.db.models import Count
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from setups import models as s_models


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        return super().default(obj)


@login_required
def home(request):
    return render(request, 'dashboard/home.html', {})


@login_required
def get_data_project_type(request):
    list = prj_models.Project.objects.values('type__name').annotate(count=Count('id'))
    data = []
    labels = []
    for item in list:
        labels.append(item['type__name'])
        data.append(item['count'])
    return JsonResponse({
        'data': data,
        'labels': labels
    })


@login_required
def get_data_project_region(request):
    list = prj_models.Project.objects.values('region__name').annotate(count=Count('id'))
    my_dict = {}
    data = []
    labels = []
    for item in list:
        my_dict[item['region__name']] = item['count']
    for s in s_models.Region.objects.all():
        labels.append(s.name)
        if s.name in my_dict:
            data.append(my_dict[s.name])
        else:
            data.append(0)
    return JsonResponse({
        'data': data,
        'labels': labels
    })


@login_required
def get_data_project_supplier(request):
    list = prj_models.ProjectSupplier.objects.values('supplier__name').annotate(count=Count('project'))
    data = []
    labels = []
    for item in list:
        labels.append(item['supplier__name'])
        data.append(item['count'])
    return JsonResponse({
        'data': data,
        'labels': labels
    })


@login_required
def get_data_project_status(request):
    list = prj_models.Project.objects.values('status').annotate(count=Count('id'))
    my_dict = {}
    data = []
    labels = []
    for item in list:
        my_dict[item['status']] = item['count']
    for s in prj_models.PROJECT_STATUS_LIST:
        labels.append(s[1])
        if s[0] in my_dict:
            data.append(my_dict[s[0]])
        else:
            data.append(0)
    return JsonResponse({
        'data': data,
        'labels': labels
    })
