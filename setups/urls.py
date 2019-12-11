from django.urls import path
from . import views
from . import models
from django.views.generic import ListView

urlpatterns = [
    path('', views.home, name='setups-home'),
    path('type/create', views.TypeCreateView.as_view(), name='setups-type-create'),
    path('authority/create', views.AuthorityCreateView.as_view(), name='setups-authority-create'),
    path('consultant/create', views.ConsultantCreateView.as_view(), name='setups-consultant-create'),
    path('region/create', views.RegionCreateView.as_view(), name='setups-region-create'),
    path('district/create', views.DistrictCreateView.as_view(), name='setups-district-create'),
    path('region/districts', views.load_districts, name='setups-load-districts'),
    path('supplier/create', views.SupplierCreateView.as_view(), name='setups-supplier-create'),
    path('financer/create', views.FinancerCreateView.as_view(), name='setups-financer-create'),
    path('contractor/create', views.ContractorCreateView.as_view(), name='setups-contractor-create'),
    path('status/create', views.StatusCreateView.as_view(), name='setups-status-create'),
    path('size/create', views.SizeCreateView.as_view(), name='setups-size-create'),
]
for model in models.SETUPS_LIST:
    if model in ['size', 'status']:
        tmpl = 'setups/entity_withcode_list.html'
    elif model in ['district']:
        tmpl = 'setups/entity_district_list.html'
    elif model in ['region', 'type']:
        tmpl = 'setups/entity_regiontype_list.html'
    else:
        tmpl = 'setups/entity_contactperson_list.html'

    urlpatterns.append(path(f'generic/{model}/create', views.SetupGenericCreateView.as_view(model=eval(f'models.{model.capitalize()}')), name=f'setups-{model}-create'))
    urlpatterns.append(path(f'generic/{model}/update/<pk>', views.SetupGenericUpdateView.as_view(model=eval(f'models.{model.capitalize()}')), name=f'setups-{model}-update'))
    urlpatterns.append(path(f'generic/{model}/list', ListView.as_view(template_name=tmpl, model=eval(f'models.{model.capitalize()}')), name=f'setups-{model}-list'))
