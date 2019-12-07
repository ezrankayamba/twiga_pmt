from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.shortcuts import get_object_or_404
from . import models
from . import forms
from django.urls import reverse
from . import filters


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
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm

    def form_valid(self, form):
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


class ProjectSupplierCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.ProjectSupplier
    fields = ['supplier', 'price', 'quantity']

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
    fields = ['supplier', 'price', 'quantity']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setup_url'] = reverse('setups-supplier-create')
        print('Url: ', context['setup_url'])
        return context

    def form_valid(self, form):
        project = get_object_or_404(models.Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super(ProjectSupplierUpdateView, self).form_valid(form)
