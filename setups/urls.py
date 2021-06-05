from django.urls import path
from . import views
from . import models
from django.views.generic import ListView

urlpatterns = [
    path('', views.home, name='setups-home'),
    path('popup/region/districts', views.load_districts, name='popup-setups-load-districts'),
]

for model in models.SETUPS_LIST:
    if model in ['status']:
        tmpl = 'setups/entity_status_list.html'
    elif model in ['size']:
        tmpl = 'setups/entity_coded_list.html'
    elif model in ['district']:
        tmpl = 'setups/entity_district_list.html'
    elif model in ['region', 'type']:
        tmpl = 'setups/entity_named_list.html'
    else:
        tmpl = 'setups/entity_contactperson_list.html'

    urlpatterns.append(path(f'popup/{model}/create', views.SetupPopupGenericCreateView.as_view(model=eval(f'models.{model.capitalize()}')), name=f'popup-setups-{model}-create'))
    urlpatterns.append(path(f'popup/{model}/update/<pk>', views.SetupPopupGenericUpdateView.as_view(model=eval(f'models.{model.capitalize()}')), name=f'popup-setups-{model}-update'))
    urlpatterns.append(path(f'generic/{model}/create', views.SetupGenericCreateView.as_view(model=eval(f'models.{model.capitalize()}')), name=f'setups-{model}-create'))
    urlpatterns.append(path(f'generic/{model}/update/<pk>', views.SetupGenericUpdateView.as_view(model=eval(f'models.{model.capitalize()}')), name=f'setups-{model}-update'))
    urlpatterns.append(path(f'generic/{model}/list', ListView.as_view(extra_context={'name': model, 'add_url': f'setups-{model}-create', 'update_url': f'setups-{model}-update',
                       'delete_url': f'setups-{model}-delete'}, template_name=tmpl, model=eval(f'models.{model.capitalize()}')), name=f'setups-{model}-list'))
    urlpatterns.append(path(f'generic/{model}/delete/<pk>', views.SetupGenericDeleteView.as_view(model=eval(f'models.{model.capitalize()}')), name=f'setups-{model}-delete'))
