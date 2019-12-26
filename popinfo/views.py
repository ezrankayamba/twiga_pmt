from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from setups import models as s_models


def home(request):
    return render(request, 'popinfo/home.html', {})


@login_required
def admin(request):
    context = {
        'suppliers': s_models.Supplier.objects.all()
    }
    return render(request, 'popinfo/admin.html', context=context)
