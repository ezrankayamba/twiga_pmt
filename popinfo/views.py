from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from setups import models as s_models
from django.http import HttpResponse
import os
from . import forms
from PIL import Image
from datetime import datetime
import qrcode
import tempfile
from django.http import JsonResponse
from . import imports
from . import models


def home(request):
    return render(request, 'popinfo/home.html', {})


@login_required
def admin(request):
    context = {
        'award_session': models.AwardSession.objects.first()
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


def generate_qr(request):
    if request.method == 'POST':
        form = forms.QRForm(request.POST)
        if form.is_valid():
            img_id = datetime.now().strftime("%Y%m%d%H%M%S")
            with tempfile.TemporaryFile() as fp:
                out_file = f'QR_{img_id}.png'
                text = form.cleaned_data['text']
                image_data = qrcode.make(text)
                image_data.save(out_file)
                image_data = open(out_file, "rb").read()
                response = HttpResponse(image_data, content_type="image/png")
                response['Content-Disposition'] = f'attachment; filename={out_file}'
                os.remove(out_file)
                return response
    else:
        form = forms.QRForm()
    return render(request, 'popinfo/generate_qr_form.html', {'form': form})


def replace_awards(request):
    if request.method == "POST":
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            imports.import_n_replace(file)
            return JsonResponse({
                'status': 'success',
                'file': file.name
            })

    return JsonResponse({
        'status': 'fail',
        'file': 'Form not valid or invalid method'
    })
