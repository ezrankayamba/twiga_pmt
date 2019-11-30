from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from . import models


@login_required
def home(request):
    return render(request, 'projects/home.html', {})


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = models.Project
    template_name = 'projects/home.html'
    context_object_name = 'projects'
    ordering = ['-name']
    paginate_by = 10


class ProjectCreateView(generic.CreateView):
    model = models.Project
    fields = ['name', 'type', 'region', 'municipal', 'town', 'duration']


class ProjectUpdateView(generic.UpdateView):
    model = models.Project
    fields = ['name', 'type', 'region', 'municipal', 'town', 'duration']


class ProjectDetailView(generic.DetailView):
    model = models.Project
    context_object_name = 'prj'
