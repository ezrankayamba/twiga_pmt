from django.urls import path
from . import views
from django_filters.views import FilterView
from . import models

urlpatterns = [
    path('', views.home, name='projects-home'),
    # path('', views.ProjectListView.as_view(), name='projects-home'),
    path('export', views.export_projects, name='projects-export'),
    path('create/', views.ProjectCreateView.as_view(), name='projects-create'),
    path('detail/<pk>', views.ProjectDetailView.as_view(), name='projects-detail'),
    path('update/<pk>', views.ProjectUpdateView.as_view(), name='projects-update'),
    # path('<project_id>/contractor/create', views.ProjectContractorCreateView.as_view(), name='projects-contractor-create'),
    # path('<project_id>/contractor/update/<pk>', views.ProjectContractorUpdateView.as_view(), name='projects-contractor-update'),
    # path('<project_id>/financer/create', views.ProjectFinancerCreateView.as_view(), name='projects-financer-create'),
    # path('<project_id>/financer/update/<pk>', views.ProjectFinancerUpdateView.as_view(), name='projects-financer-update'),
    # path('<project_id>/supplier/create', views.ProjectSupplierCreateView.as_view(), name='projects-supplier-create'),
    # path('<project_id>/supplier/update/<pk>', views.ProjectSupplierUpdateView.as_view(), name='projects-supplier-update'),
    # path('<project_id>/consultant/create', views.ProjectConsultantCreateView.as_view(), name='projects-consultant-create'),
    # path('<project_id>/consultant/update/<pk>', views.ProjectConsultantUpdateView.as_view(), name='projects-consultant-update'),
    path('<project_id>/audit/create', views.ProjectAuditCreateView.as_view(), name='projects-audit-create'),
]

for name in ['consultant', 'contractor', 'financer', 'supplier']:
    urlpatterns.append(path(f'{name}/<pk>/delete', views.ProjectSetupGenericDeleteView.as_view(model=eval(f'models.Project{name.capitalize()}')), name=f'projects-{name}-delete'))
    urlpatterns.append(path(f'<project_id>/{name}/create', views.SetupGenericCreateView.as_view(model=eval(f'models.Project{name.capitalize()}')), name=f'projects-{name}-create'))
    urlpatterns.append(path(f'<project_id>/{name}/update/<pk>', views.SetupGenericUpdateView.as_view(model=eval(f'models.Project{name.capitalize()}')), name=f'projects-{name}-update'))
