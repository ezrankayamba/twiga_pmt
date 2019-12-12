from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.shortcuts import get_object_or_404
from . import models
from . import forms
from django.urls import reverse, reverse_lazy
from . import filters
from .resources import ProjectResource
from django.http import HttpResponse
from datetime import datetime
from . import exports
import re


@login_required
def home(request):
    projects = models.Project.objects.all()
    prj_filter = filters.ProjectFilter(request.POST, queryset=projects)
    return render(request, 'projects/home.html', {'filter': prj_filter})


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = models.Project
    template_name = 'projects/home.html'
    context_object_name = 'projects'
    ordering = ['-name']
    paginate_by = 10


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Project
    context_object_name = 'prj'


class ProjectContractorCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.ProjectContractor
    fields = ['contractor', 'sub_contractor']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setup_url'] = reverse('setups-contractor-create')
        return context

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(ProjectContractorCreateView, self).form_valid(form)


class ProjectContractorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.ProjectContractor
    fields = ['contractor', 'sub_contractor']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setup_url'] = reverse('setups-contractor-create')
        return context

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(ProjectContractorUpdateView, self).form_valid(form)


class ProjectFinancerCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.ProjectFinancer
    fields = ['financer']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setup_url'] = reverse('setups-financer-create')
        return context

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(ProjectFinancerCreateView, self).form_valid(form)


class ProjectFinancerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.ProjectFinancer
    fields = ['financer']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setup_url'] = reverse('setups-financer-create')
        return context

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(ProjectFinancerUpdateView, self).form_valid(form)


class ProjectConsultantCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.ProjectConsultant
    fields = ['consultant']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setup_url'] = reverse('setups-consultant-create')
        return context

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(ProjectConsultantCreateView, self).form_valid(form)


class ProjectConsultantUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.ProjectConsultant
    fields = ['consultant']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setup_url'] = reverse('setups-consultant-create')
        return context

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(ProjectConsultantUpdateView, self).form_valid(form)


class ProjectSupplierCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.ProjectSupplier
    fields = ['supplier', 'price', 'quantity', 'under']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setup_url'] = reverse('setups-supplier-create')
        print('Url: ', context['setup_url'])
        return context

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(ProjectSupplierCreateView, self).form_valid(form)


class ProjectSupplierUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.ProjectSupplier
    fields = ['supplier', 'price', 'quantity', 'under']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setup_url'] = reverse('setups-supplier-create')
        print('Url: ', context['setup_url'])
        return context

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(ProjectSupplierUpdateView, self).form_valid(form)


class ProjectAuditCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.ProjectAudit
    form_class = forms.ProjectAuditCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        form.instance.manual = True
        form.instance.logged_by = self.request.user
        form.instance.other = 'Manual Audit'
        return super(ProjectAuditCreateView, self).form_valid(form)


class SetupGenericCreateView(generic.CreateView):
    template_name = 'projects/setup_form.html'

    def get_success_url(self):
        return self.object.ger_absolute_url()

    def __init__(self, *args, **kwargs):
        super(SetupGenericCreateView, self).__init__(*args, **kwargs)
        name = self.model.__name__.lower()

        if name in ['projectcontractor']:
            self.fields = ['contractor', 'sub_contractor']
        elif name in ['projectsupplier']:
            self.fields = ['supplier', 'price', 'quantity', 'under']
        else:
            self.fields = [name.replace('project', '')]

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(SetupGenericCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model.__name__.replace('Project', '')
        context['count'] = self.model.objects.all().count()
        print(self.model.objects.all())
        return context


class SetupGenericUpdateView(generic.UpdateView):
    template_name = 'projects/setup_form.html'

    def get_success_url(self):
        return self.object.ger_absolute_url()

    def __init__(self, *args, **kwargs):
        super(SetupGenericUpdateView, self).__init__(*args, **kwargs)
        name = self.model.__name__.lower()

        if name in ['projectcontractor']:
            self.fields = ['contractor', 'sub_contractor']
        elif name in ['projectsupplier']:
            self.fields = ['supplier', 'price', 'quantity', 'under']
        else:
            self.fields = [name.replace('project', '')]

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(SetupGenericUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model.__name__.replace('Project', '')
        context['count'] = self.model.objects.all().count()
        print(self.model.objects.all())
        return context


class ProjectSetupGenericDeleteView(generic.DeleteView):
    def get_success_url(self):
        project = self.object.project
        return reverse_lazy('projects-detail', kwargs={'pk': project.id})


def export_projects(request):
    export_id = datetime.now().strftime("%Y%m%d%H%M%S")
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{export_id}_Projects.xlsx"'
    xlsx_data = exports.projects_report(request)
    response.write(xlsx_data)
    return response
