from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_views.UserListView.as_view(), name='users-list'),
    path('register/', user_views.UserCreateView.as_view(), name='users-create'),
    path('update/<pk>', user_views.UserUpdateView.as_view(), name='users-update'),
    path('roles/', user_views.RoleListView.as_view(), name='role-list'),
    path('roles/create', user_views.RoleCreateView.as_view(), name='role-create'),
    path('roles/detail/<pk>', user_views.RoleDetailView.as_view(), name='role-detail'),
    path('roles/privileges-update', user_views.role_privileges_update, name='role-privileges-update'),
    path('profile/', user_views.profile, name='users-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    path('changemypassword/', user_views.ChangeMyPasswordView.as_view(), name='users-change-password'),
    path('forgotpassword/', user_views.ForgotPasswordView.as_view(), name='forgot-password'),
]
