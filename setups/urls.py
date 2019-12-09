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
    path('supplier/create', views.SupplierCreateView.as_view(), name='setups-supplier-create'),
    path('financer/create', views.FinancerCreateView.as_view(), name='setups-financer-create'),
    path('contractor/create', views.ContractorCreateView.as_view(), name='setups-contractor-create'),
    path('status/create', views.StatusCreateView.as_view(), name='setups-status-create'),
    path('size/create', views.SizeCreateView.as_view(), name='setups-size-create'),
]
