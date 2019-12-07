from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . import models


@receiver(post_save, sender=models.Project)
def project_created(sender, instance, created, **kwargs):
    prj = instance
    if created:
        models.ProjectAudit.objects.create(
            project=prj,
            remarks=prj.remarks,
            demanded=prj.quantity_demanded,
            supplied=prj.quantity_supplied,
            balance=prj.quantity_demanded - prj.quantity_supplied,
            other='Created',
            logged_by=prj.created_by)
    else:
        models.ProjectAudit.objects.create(
            project=prj,
            remarks=prj.remarks,
            demanded=prj.quantity_demanded,
            supplied=prj.quantity_supplied,
            balance=prj.quantity_demanded - prj.quantity_supplied,
            other='Updated',
            logged_by=prj.updated_by)
