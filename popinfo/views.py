from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from setups import models as s_models
from django.http import HttpResponse
import os
# import numpy as np
from PIL import Image


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


def merge_images_vertically(imgs, out_file):
    widths, heights = zip(*(i.size for i in imgs))
    width_of_new_image = min(widths)
    height_of_new_image = sum(heights)
    new_im = Image.new('RGB', (width_of_new_image, height_of_new_image))
    new_pos = 0
    for im in imgs:
        new_im.paste(im, (0, new_pos))
        new_pos += im.size[1]
    new_im.save(out_file)


def tna_info(request):
    path = './core/static/core/images/tza_info'
    out_file = 'out.jpeg'
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    if out_file in files:
        pass
    else:
        imgs = [Image.open(os.path.join(path, im)) for im in files]
        merge_images_vertically(imgs, os.path.join(path, out_file))
    image_data = open(os.path.join(path, out_file), "rb").read()
    response = HttpResponse(image_data, content_type="image/jpeg")
    return response
