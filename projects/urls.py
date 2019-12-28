from django.urls import path
from . import views
from django_filters.views import FilterView
from . import models

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='projects-home'),
    path('export', views.export_projects, name='projects-export'),
    path('import', views.import_projects, name='projects-import'),
    path('create/', views.ProjectCreateView.as_view(), name='projects-create'),
    path('detail/<pk>', views.ProjectDetailView.as_view(), name='projects-detail'),
    path('alert/<pk>', views.ProjectDetailAlertView.as_view(), name='projects-detail-alert'),
    path('update/<pk>', views.ProjectUpdateView.as_view(), name='projects-update'),
    path('<project_id>/audit/create', views.ProjectAuditCreateView.as_view(), name='projects-audit-create'),
]

for name in ['consultant', 'contractor', 'financer', 'supplier', 'image']:
    if name == 'image':
        tmpl = 'projects/image_form.html'
    else:
        tmpl = 'projects/setup_form.html'
    urlpatterns.append(path(f'{name}/<pk>/delete', views.ProjectSetupGenericDeleteView.as_view(template_name=tmpl, model=eval(f'models.Project{name.capitalize()}')), name=f'projects-{name}-delete'))
    urlpatterns.append(path(f'<project_id>/{name}/create', views.SetupGenericCreateView.as_view(template_name=tmpl, model=eval(f'models.Project{name.capitalize()}')), name=f'projects-{name}-create'))
    urlpatterns.append(path(f'<project_id>/{name}/update/<pk>', views.SetupGenericUpdateView.as_view(model=eval(f'models.Project{name.capitalize()}')), name=f'projects-{name}-update'))
