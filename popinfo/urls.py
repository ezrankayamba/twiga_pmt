from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='popinfo-home'),
    path('admin', views.admin, name='popinfo-admin'),
]
