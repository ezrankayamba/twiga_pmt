from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='setups-home'),
    path('type/create', views.TypeCreateView.as_view(), name='setups-type-create'),
    path('authority/create', views.AuthorityCreateView.as_view(), name='setups-authority-create'),
    path('consultant/create', views.ConsultantCreateView.as_view(), name='setups-consultant-create'),
    path('region/create', views.RegionCreateView.as_view(), name='setups-region-create'),
    path('district/create', views.DistrictCreateView.as_view(), name='setups-district-create'),
    path('region/districts', views.load_districts, name='setups-load-districts'),
]
