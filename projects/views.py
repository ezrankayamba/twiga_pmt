from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.shortcuts import get_object_or_404
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
    fields = ['name', 'type', 'region', 'municipal', 'town', 'duration', 'authority', 'consultant']


class ProjectUpdateView(generic.UpdateView):
    model = models.Project
    fields = ['name', 'type', 'region', 'municipal', 'town', 'duration', 'authority', 'consultant']


class ProjectDetailView(generic.DetailView):
    model = models.Project
    context_object_name = 'prj'


class ProjectContractorCreateView(generic.CreateView):
    model = models.ProjectContractor
    fields = ['contractor', 'sub_contractor']

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(ProjectContractorCreateView, self).form_valid(form)


class ProjectContractorUpdateView(generic.UpdateView):
    model = models.ProjectContractor
    fields = ['contractor', 'sub_contractor']

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(ProjectContractorUpdateView, self).form_valid(form)


class ProjectFinancerCreateView(generic.CreateView):
    model = models.ProjectFinancer
    fields = ['financer']

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(ProjectFinancerCreateView, self).form_valid(form)


class ProjectFinancerUpdateView(generic.UpdateView):
    model = models.ProjectFinancer
    fields = ['financer']

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(ProjectFinancerUpdateView, self).form_valid(form)


class ProjectSupplierCreateView(generic.CreateView):
    model = models.ProjectSupplier
    fields = ['supplier', 'price', 'remarks']

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(ProjectSupplierCreateView, self).form_valid(form)


class ProjectSupplierUpdateView(generic.UpdateView):
    model = models.ProjectSupplier
    fields = ['supplier']

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(ProjectSupplierUpdateView, self).form_valid(form)
