from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.views.decorators.csrf import csrf_exempt


@login_required
def home(request):
    return render(request, 'setups/home.html', {})


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


class TypeUpdateView(generic.UpdateView):
    model = models.Type
    fields = ['name']
