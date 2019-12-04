from django.db import models
from django.urls import reverse
from setups import models as s_models

PROJECT_STATUS_LIST = (('INT', "Initiated"), ('ONG', "Ongoing"), ('CMP', "Completed"))


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    start_date = models.DateField(null=True)
    type = models.ForeignKey(to=s_models.Type, related_name="projects", on_delete=models.PROTECT)
    status = models.CharField(max_length=10, default='INT', choices=PROJECT_STATUS_LIST)
    region = models.ForeignKey(to=s_models.Region, related_name="projects", on_delete=models.PROTECT, null=True)
    district = models.ForeignKey(to=s_models.District, related_name="projects", on_delete=models.PROTECT, null=True)
    town = models.CharField(max_length=40, null=True)
    duration = models.DecimalField(decimal_places=2, max_digits=10, default=1, verbose_name=('Duration(Years)'))
    authority = models.ForeignKey(to=s_models.Authority, related_name="projects", on_delete=models.PROTECT, null=True)
    consultant = models.ForeignKey(to=s_models.Consultant, related_name="projects", on_delete=models.PROTECT, null=True)
    remarks = models.CharField(max_length=1000, null=True, blank=True)

    def get_status(self):
        for en in PROJECT_STATUS_LIST:
            if(en[0] == self.status):
                return en[1]
        return 'Unknown'

    def get_location(self):
        return f'{self.region}, {self.district}, {self.town}'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects-detail', kwargs={'pk': self.pk})


class ProjectContractor(models.Model):
    project = models.ForeignKey(to=Project, related_name="project_contractors", on_delete=models.PROTECT)
    contractor = models.ForeignKey(to=s_models.Contractor, related_name="project_contractors", on_delete=models.PROTECT)
    sub_contractor = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('projects-detail', kwargs={'pk': self.project.id})


class ProjectFinancer(models.Model):
    project = models.ForeignKey(to=Project, related_name="project_financers", on_delete=models.PROTECT)
    financer = models.ForeignKey(to=s_models.Financer, related_name="project_financers", on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('projects-detail', kwargs={'pk': self.project.id})


class ProjectSupplier(models.Model):
    project = models.ForeignKey(to=Project, related_name="project_suppliers", on_delete=models.PROTECT)
    supplier = models.ForeignKey(to=s_models.Supplier, related_name="project_suppliers", on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=1, verbose_name=('Price(TZS)'))
    remarks = models.CharField(max_length=255, verbose_name=('Specific Requirement'))

    def get_absolute_url(self):
        return reverse('projects-detail', kwargs={'pk': self.project.id})
