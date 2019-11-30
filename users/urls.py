from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', user_views.register, name='users-register'),
    path('profile/', user_views.profile, name='users-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    path('changemypassword/', user_views.ChangeMyPasswordView.as_view(), name='users-change-password'),
]
