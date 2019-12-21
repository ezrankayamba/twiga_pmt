from django.urls import path, include
from . import views

urlpatterns = [
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('regions/', views.RegionList.as_view()),
    path('projects/<region_id>/', views.ProjectList.as_view()),
]
