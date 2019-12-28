from django.shortcuts import render, redirect
from django.urls import reverse
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
from . import imports
from django.http import JsonResponse
from django_filters.views import FilterView
from django.core.paginator import Paginator
from datetime import datetime
import openpyxl


@login_required
def home(request):
    projects = models.Project.objects.all()
    prj_filter = filters.ProjectFilter(request.POST, queryset=projects)
    return render(request, 'projects/home.html', {'filter': prj_filter})


class ProjectListView(LoginRequiredMixin, FilterView):
    model = models.Project
    filterset_class = filters.ProjectFilter
    template_name = 'projects/home.html'
    context_object_name = 'projects'
    ordering = ['-name']
    paginate_by = 8

    def get_queryset(self):
        self.projects = models.Project.objects.all()
        self.prj_filter = filters.ProjectFilter(self.request.POST, queryset=self.projects)
        qs = self.prj_filter.qs
        return qs

    def get_context_data(self, **kwargs):
        qs = self.get_queryset()
        kwargs['total_projects'] = qs.count()
        ctx = super(ProjectListView, self).get_context_data(**kwargs)
        return ctx

    def post(self, request, *args, **kwargs):
        qs = self.get_queryset()
        paginator = Paginator(qs, self.paginate_by)
        qs2 = paginator.get_page(request.POST.get('page', 1))
        return render(request, self.template_name, {
            'filter': self.prj_filter,
            'projects': qs2,
            'is_paginated': qs.count() > self.paginate_by,
            'total_projects': qs.count(),
            'page_obj': qs2
        })


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


class ProjectDetailAlertView(generic.DetailView):
    model = models.Project
    context_object_name = 'prj'
    template_name = 'projects/project_detail_alert.html'


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
        return self.object.get_absolute_url()

    def __init__(self, *args, **kwargs):
        super(SetupGenericCreateView, self).__init__(*args, **kwargs)
        name = self.model.__name__.lower()

        if name in ['projectcontractor']:
            self.fields = ['contractor', 'sub_contractor']
        elif name in ['projectsupplier']:
            self.fields = ['supplier', 'price', 'quantity', 'under']
        elif name in ['projectimage']:
            self.fields = ['image', 'title']
        else:
            self.fields = [name.replace('project', '')]

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(SetupGenericCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.model.__name__.replace('Project', '')
        context['model_name'] = name
        context['count'] = self.model.objects.all().count()
        if name.lower() != 'image':
            context['setup_url'] = reverse(f'popup-setups-{name.lower()}-create')
        return context


class SetupGenericUpdateView(generic.UpdateView):
    template_name = 'projects/setup_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()

    def __init__(self, *args, **kwargs):
        super(SetupGenericUpdateView, self).__init__(*args, **kwargs)
        name = self.model.__name__.lower()

        if name in ['projectcontractor']:
            self.fields = ['contractor', 'sub_contractor']
        elif name in ['projectsupplier']:
            self.fields = ['supplier', 'price', 'quantity', 'under']
        elif name in ['projectimage']:
            self.fields = ['image', 'title']
        else:
            self.fields = [name.replace('project', '')]

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        print('Instance: ', form.instance)
        return super(SetupGenericUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.model.__name__.replace('Project', '')
        context['model_name'] = name
        context['count'] = self.model.objects.all().count()
        if name.lower() != 'image':
            context['setup_url'] = reverse(f'popup-setups-{name.lower()}-create')
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


def import_projects(request):
    if request.method == "POST":
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            imports.import_projects(excel_file)
            return JsonResponse({
                'status': 'success',
                'file': excel_file.name
            })

    return JsonResponse({
        'status': 'fail',
        'file': 'Form not valid or invalid method'
    })
