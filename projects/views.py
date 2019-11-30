from django.shortcuts import render


def setups(request):
    return render(request, 'projects/setups.html', {})
