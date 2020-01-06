from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='popinfo-home'),
    path('admin', views.admin, name='popinfo-admin'),
    path('tzainfo', views.tna_info, name='popinfo-tnainfo'),
    path('qr', views.generate_qr, name='popinfo-generate-qr'),
    path('replace-awards', views.replace_awards, name='popinfo-replace-awards'),
]
