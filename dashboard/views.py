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
    si = [
        {'name': 'Projects', 'value': prj_models.Project.objects.count()},
        {'name': 'Contractors', 'value': s_models.Contractor.objects.count()},
        {'name': 'Suppliers', 'value': s_models.Supplier.objects.count()},
        {'name': 'Consultants', 'value': s_models.Consultant.objects.count()},
    ]
    return render(request, 'dashboard/home.html', {'summary_items': si})


@login_required
def map(request):
    return render(request, 'dashboard/map.html', {})


@login_required
def get_data_project_type(request):
    list = s_models.Type.objects.all()
    data = []
    labels = []
    for item in list:
        labels.append(item.name)
        data.append(item.projects.count())
    return JsonResponse({
        'data': data,
        'labels': labels
    })


@login_required
def get_data_project_list(request):
    list = prj_models.Project.objects.all()
    res = []
    for p in list:
        main = []
        for c in p.contractors.filter(sub_contractor=False):
            main.append(c.contractor.name)
        print(main)
        res.append({
            'id': p.id,
            'name': p.name,
            'lat': p.latitude,
            'lng': p.longitude,
            'qty': f'{p.quantity_demanded:,}',
            'supplied': f'{p.quantity_supplied:,}',
            'authority': p.authority.name,
            'contractors': main,
            'url': p.get_absolute_url()
        })
    return JsonResponse({'data': res})


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
def get_data_project_region_plus(request):
    list = prj_models.Project.objects.values('region__name', 'district__name').order_by('region__name', 'district__name').annotate(count=Count('id'))
    r_dict = {}
    d_dict = {}
    my_dict = {}
    data = []
    labels = []
    region_name = None
    r_count = 0
    for item in list:
        if item['region__name'] != region_name:  # switch region
            if region_name:
                r_dict[region_name] = {
                    'count': r_count,
                    'districts': d_dict
                }
            d_dict = {}
            r_count = 0
            region_name = item['region__name']
        count = item['count']
        d_dict[item['district__name']] = count
        r_count += count
    r_dict[region_name] = {
        'count': r_count,
        'districts': d_dict
    }

    regions = s_models.Region.objects.all()
    r_full_dict = {}
    for r in regions:
        labels.append(r.name)
        d_full_dict = {}
        if r.name in r_dict:
            tmp_r = r_dict[r.name]
            data.append(tmp_r['count'])
            for d in r.districts.all():
                if d.name in tmp_r['districts']:
                    d_full_dict[d.name] = tmp_r['districts'][d.name]
                else:
                    d_full_dict[d.name] = 0
            r_full_dict[r.name] = {
                'count': tmp_r['count'],
                'districts': d_full_dict
            }
        else:
            for d in r.districts.all():
                d_full_dict[d.name] = 0
            r_full_dict[r.name] = {
                'count': 0,
                'districts': d_full_dict
            }
            data.append(0)
    return JsonResponse({
        'data': data,
        'labels': labels,
        'full': r_full_dict
    })


@login_required
def get_data_project_supplier(request):
    data = []
    labels = []
    for item in s_models.Supplier.objects.all():
        labels.append(item.name)
        data.append(item.projects.count())
    return JsonResponse({
        'data': data,
        'labels': labels
    })


@login_required
def get_data_project_status(request):
    data = []
    labels = []
    for s in s_models.Status.objects.all():
        labels.append(s.name)
        data.append(s.projects.count())
    return JsonResponse({
        'data': data,
        'labels': labels
    })


@login_required
def get_data_project_size(request):
    data = []
    labels = []
    for s in s_models.Size.objects.all():
        labels.append(s.name)
        data.append(s.projects.count())
    return JsonResponse({
        'data': data,
        'labels': labels
    })
