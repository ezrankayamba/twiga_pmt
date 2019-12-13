from django.urls import path
from . import views
from . import models
from django.views.generic import ListView

urlpatterns = [
    path('', views.home, name='setups-home'),
    path('popup/type/create', views.TypeCreateView.as_view(), name='popup-setups-type-create'),
    path('popup/authority/create', views.AuthorityCreateView.as_view(), name='popup-setups-authority-create'),
    path('popup/consultant/create', views.ConsultantCreateView.as_view(), name='popup-setups-consultant-create'),
    path('popup/region/create', views.RegionCreateView.as_view(), name='popup-setups-region-create'),
    path('popup/district/create', views.DistrictCreateView.as_view(), name='popup-setups-district-create'),
    path('popup/region/districts', views.load_districts, name='popup-setups-load-districts'),
    path('popup/supplier/create', views.SupplierCreateView.as_view(), name='popup-setups-supplier-create'),
    path('popup/financer/create', views.FinancerCreateView.as_view(), name='popup-setups-financer-create'),
    path('popup/contractor/create', views.ContractorCreateView.as_view(), name='popup-setups-contractor-create'),
    path('popup/status/create', views.StatusCreateView.as_view(), name='popup-setups-status-create'),
    path('popup/size/create', views.SizeCreateView.as_view(), name='popup-setups-size-create'),
]
# print(dir(ListView))
for model in models.SETUPS_LIST:
    if model in ['size', 'status']:
        tmpl = 'setups/entity_coded_list.html'
    elif model in ['district']:
        tmpl = 'setups/entity_district_list.html'
    elif model in ['region', 'type']:
        tmpl = 'setups/entity_named_list.html'
    else:
        tmpl = 'setups/entity_contactperson_list.html'

    urlpatterns.append(path(f'generic/{model}/create', views.SetupGenericCreateView.as_view(model=eval(f'models.{model.capitalize()}')), name=f'setups-{model}-create'))
    urlpatterns.append(path(f'generic/{model}/update/<pk>', views.SetupGenericUpdateView.as_view(model=eval(f'models.{model.capitalize()}')), name=f'setups-{model}-update'))
    urlpatterns.append(path(f'generic/{model}/list', ListView.as_view(extra_context={'name': model, 'add_url': f'setups-{model}-create', 'update_url': f'setups-{model}-update', 'delete_url': f'setups-{model}-delete'}, template_name=tmpl, model=eval(f'models.{model.capitalize()}')), name=f'setups-{model}-list'))
    urlpatterns.append(path(f'generic/{model}/delete/<pk>', views.SetupGenericDeleteView.as_view(model=eval(f'models.{model.capitalize()}')), name=f'setups-{model}-delete'))
