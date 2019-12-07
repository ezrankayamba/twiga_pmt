from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('map/', views.map, name='dashboard-map'),
    path('data/project-type', views.get_data_project_type, name='data-project-type'),
    path('data/project-status', views.get_data_project_status, name='data-project-status'),
    path('data/project-supplier', views.get_data_project_supplier, name='data-project-supplier'),
    path('data/project-region', views.get_data_project_region, name='data-project-region'),
    path('data/project-region-plus', views.get_data_project_region_plus, name='data-project-region-plus'),
]
