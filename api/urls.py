from django.urls import path, include
from . import views

urlpatterns = [
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('projects/', views.ProjectList.as_view()),
]
