from django.db.models import signals as sig
from django.contrib.auth.models import User
from django.dispatch import receiver
from . import models
from django.conf import settings
import os
from PIL import Image


@receiver(sig.post_save, sender=models.Project)
def project_created(sender, instance, created, **kwargs):
    prj = instance
    if created:
        print('Creating audit for - create')
        models.ProjectAudit.objects.create(
            project=prj,
            remarks=prj.remarks,
            demanded=prj.quantity_demanded,
            supplied=prj.quantity_supplied,
            balance=prj.quantity_demanded - prj.quantity_supplied,
            other='Created',
            logged_by=prj.created_by)
    else:
        print('Creating audit for - update')
        models.ProjectAudit.objects.create(
            project=prj,
            remarks=prj.remarks,
            demanded=prj.quantity_demanded,
            supplied=prj.quantity_supplied,
            balance=prj.quantity_demanded - prj.quantity_supplied,
            other='Updated',
            logged_by=prj.updated_by)


@receiver(sig.post_delete, sender=models.ProjectImage)
def remove_image(sender, instance, using, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
            print(f'Successfully removed the image at: {instance.image.path}')


@receiver(sig.post_save, sender=models.ProjectImage)
def resize_image(sender, instance, created, raw, using, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            size = 640, 480
            print(f'Image file: {instance.image.path}')
            infile = os.path.join(settings.MEDIA_ROOT, instance.image.name)
            image = Image.open(infile)
            image = image.resize(size, Image.ANTIALIAS)
            image.save(instance.image.path, image.format, quality=72)
            print(
                f'Successfully resized 640 X 480 image at: {instance.image.path}')
