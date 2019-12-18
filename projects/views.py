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
from django.http import JsonResponse


@login_required
def home(request):
    projects = models.Project.objects.all()
    prj_filter = filters.ProjectFilter(request.POST, queryset=projects)
    return render(request, 'projects/home.html', {'filter': prj_filter})


def get_projects_json(request):
    projects = models.Project.objects.all()
    data = []
    for prj in projects:
        data.append({
            'id': prj.id,
            'name': prj.name,
            'region_id': prj.region_id,
            'region_name': prj.region.name,
            'lat': prj.latitude,
            'lng': prj.longitude
        })
    return JsonResponse(data, safe=False)


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
