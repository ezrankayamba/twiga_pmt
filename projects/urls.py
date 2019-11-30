from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='projects-home'),
    path('create/', views.ProjectCreateView.as_view(), name='projects-create'),
    path('detail/<pk>', views.ProjectDetailView.as_view(), name='projects-detail'),
    path('update/<pk>', views.ProjectUpdateView.as_view(), name='projects-update'),
]
