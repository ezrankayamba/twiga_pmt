from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


@login_required
def home(request):
    ctx = {}
    for model in models.SETUPS_LIST:
        Cls = eval(f'models.{model.capitalize()}')
        ctx[f'{model}_count'] = Cls.objects.count()
    return render(request, 'setups/home.html', ctx)


@csrf_exempt
def load_districts(request):
    region_id = request.GET.get('region')
    print('RegionID: ', region_id)
    districts = models.District.objects.filter(region_id=region_id).order_by('name')
    return render(request, 'setups/district_dropdown_list_options.html', {'districts': districts})


class TypeCreateView(generic.CreateView):
    model = models.Type
    template_name = 'setups/popups/type_form.html'
    fields = ['name']

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(f'<script>opener.closePopup({instance.id}, "{instance.name}", "#id_type");</script>')


class AuthorityCreateView(generic.CreateView):
    model = models.Authority
    template_name = 'setups/popups/authority_form.html'
    fields = ['name']

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(f'<script>opener.closePopup({instance.id}, "{instance.name}", "#id_authority");</script>')


class ConsultantCreateView(generic.CreateView):
    model = models.Consultant
    template_name = 'setups/popups/consultant_form.html'
    fields = ['name']

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(f'<script>opener.closePopup({instance.id}, "{instance.name}", "#id_consultant");</script>')


class SupplierCreateView(generic.CreateView):
    model = models.Supplier
    template_name = 'setups/popups/supplier_form.html'
    fields = ['name']

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(f'<script>opener.closePopup({instance.id}, "{instance.name}", "#id_supplier");</script>')


class FinancerCreateView(generic.CreateView):
    model = models.Financer
    template_name = 'setups/popups/financer_form.html'
    fields = ['name']

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(f'<script>opener.closePopup({instance.id}, "{instance.name}", "#id_financer");</script>')


class ContractorCreateView(generic.CreateView):
    model = models.Contractor
    template_name = 'setups/popups/contractor_form.html'
    fields = ['name']

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(f'<script>opener.closePopup({instance.id}, "{instance.name}", "#id_contractor");</script>')


class RegionCreateView(generic.CreateView):
    model = models.Region
    template_name = 'setups/popups/region_form.html'
    fields = ['name']

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(f'<script>opener.closePopup({instance.id}, "{instance.name}", "#id_region");</script>')


class DistrictCreateView(generic.CreateView):
    model = models.District
    template_name = 'setups/popups/district_form.html'
    fields = ['name']

    def form_valid(self, form):
        region = get_object_or_404(models.Region, id=self.request.GET.get('region'))
        form.instance.region = region
        instance = form.save()
        return HttpResponse(f'<script>opener.closePopup({instance.id}, "{instance.name}", "#id_district");</script>')


class SizeCreateView(generic.CreateView):
    model = models.Size
    template_name = 'setups/popups/size_form.html'
    fields = ['code', 'name']

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(f'<script>opener.closePopup({instance.id}, "{instance.name}", "#id_size");</script>')


class StatusCreateView(generic.CreateView):
    model = models.Status
    template_name = 'setups/popups/status_form.html'
    fields = ['code', 'name']

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(f'<script>opener.closePopup({instance.id}, "{instance.name}", "#id_status");</script>')


class TypeUpdateView(generic.UpdateView):
    model = models.Type
    fields = ['name']


class SetupGenericListView(generic.ListView):
    # template_name = 'setups/setup_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        print('context', context)
        return context


class SetupGenericCreateView(generic.CreateView):
    template_name = 'setups/setup_form.html'

    def __init__(self, *args, **kwargs):
        super(SetupGenericCreateView, self).__init__(*args, **kwargs)
        name = self.model.__name__.lower()
        self.success_url = reverse(f'setups-{name}-list')
        if name in ['size', 'status']:
            self.fields = ['code', 'name']
        elif name in ['district']:
            self.fields = ['name', 'region']
        elif name in ['region', 'type']:
            self.fields = ['name']
        else:
            self.fields = ['name', 'contact_person', 'position', 'phone', 'email', 'location']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        return context


class SetupGenericUpdateView(generic.UpdateView):
    template_name = 'setups/setup_form.html'

    def __init__(self, *args, **kwargs):
        super(SetupGenericUpdateView, self).__init__(*args, **kwargs)
        name = self.model.__name__.lower()
        self.success_url = reverse(f'setups-{name}-list')

        if name in ['size', 'status']:
            self.fields = ['code', 'name']
        elif name in ['district']:
            self.fields = ['name', 'region']
        elif name in ['region', 'type']:
            self.fields = ['name']
        else:
            self.fields = ['name', 'contact_person', 'position', 'phone', 'email', 'location']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        context['count'] = self.model.objects.all().count()
        print(self.model.objects.all())
        return context


class SetupGenericDeleteView(generic.DeleteView):

    def __init__(self, *args, **kwargs):
        super(SetupGenericDeleteView, self).__init__(*args, **kwargs)
        name = self.model.__name__.lower()
        self.success_url = reverse(f'setups-{name}-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model.__name__
        return context
