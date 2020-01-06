from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PasswordChangeForm, UserProfileForm, UserCreateForm
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from core.models import Config
from . import models
from . import choices
from django.urls import reverse


@login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        form.set_password = Config.objects.get(name='INITIAL_PASSWORD').value
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'You have created {username} account successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


class ChangeMyPasswordView(LoginRequiredMixin, FormView):
    form_class = PasswordChangeForm
    template_name = 'users/changemypassword_form.html'
    success_url = '/'

    def form_valid(self, form):
        data = form.cleaned_data
        print('Cleaned data: ', form.cleaned_data)
        user = User.objects.filter(pk=self.request.user.id).first()
        user.set_password(data['new_password'])
        user.save()
        return super().form_valid(form)


class RoleListView(LoginRequiredMixin, ListView):
    model = models.Role


class RoleDetailView(LoginRequiredMixin, DetailView):
    model = models.Role

    def get_context_data(self, **kwargs):
        all_privs = []
        print(kwargs['object'])
        for priv in choices.PRIVILEGE_CHOICES:
            try:
                obj = models.RolePrivilege.objects.get(privilege=priv[0], role=kwargs['object'])
                print('Exist: ', obj.role.name)
            except models.RolePrivilege.DoesNotExist:
                obj = None
            all_privs.append({'privilege': priv, 'on': obj != None})
        print(all_privs)
        kwargs['privileges'] = all_privs
        ctx = super(RoleDetailView, self).get_context_data(**kwargs)
        return ctx


class RoleCreateView(LoginRequiredMixin, CreateView):
    model = models.Role
    fields = '__all__'


@login_required
def role_privileges_update(request):
    if request.method == 'POST':
        print(request.POST)
        role_id = request.POST.get('role_id', None)
        selected_list = request.POST.getlist('on')
        models.RolePrivilege.objects.filter(role_id=role_id).delete()
        for p in selected_list:
            print('Creating: ', p)
            rp = models.RolePrivilege(role_id=role_id, privilege=p)
            rp.save()
        return redirect(reverse('role-detail', kwargs={'pk': role_id}))


class UserListView(LoginRequiredMixin, ListView):
    model = models.User
    template_name = 'users/user_list.html'


class UserCreateView(LoginRequiredMixin, CreateView):
    template_name = 'users/create_user_form.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        user = User.objects.create_user(username=data['username'], email=data['email'], password=Config.objects.get(name='INITIAL_PASSWORD').value)
        p = user.profile
        p.role = data['role']
        p.save()
        return redirect('users-list')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update_user_form.html'
    form_class = UserUpdateForm
    model = User

    def get_initial(self):
        return {'role': self.get_object().profile.role}

    def form_valid(self, form):
        data = form.cleaned_data
        user = self.get_object()
        user.email = data['email']
        user.save()
        p = user.profile
        p.role = data['role']
        p.save()
        return redirect('users-list')
