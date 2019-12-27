from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from setups import models as s_models


def home(request):
    return render(request, 'popinfo/home.html', {})


@login_required
def admin(request):
    suppliers = []
    for supplier in s_models.Supplier.objects.all():
        count_all = supplier.projects.count()
        if count_all == 0:
            count_all = 1
        flt = list(filter(lambda x: x.project.status.name == 'Completed', supplier.projects.all()))
        count_completed = len(flt)

        suppliers.append({
            'id': supplier.id,
            'name': supplier.name,
            'age': 28,
            'projects': count_all,
            'performance': 100 * count_completed / count_all
        })

    context = {
        'suppliers': suppliers
    }
    return render(request, 'popinfo/admin.html', context=context)
