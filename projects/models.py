from django.db import models
from django.urls import reverse
from setups import models as s_models
from datetime import datetime, date
from datetime import timedelta
import decimal
from django.contrib.auth.models import User
from PIL import Image
from core.models import UpperCaseCharField


def initial_status():
    return s_models.Status.objects.get(code='INT')


class Project(models.Model):
    name = UpperCaseCharField(max_length=255, unique=True)
    start_date = models.DateField(blank=True, null=True)
    type = models.ForeignKey(to=s_models.Type, related_name="projects", on_delete=models.PROTECT)
    status = models.ForeignKey(to=s_models.Status, related_name="projects", on_delete=models.PROTECT, default=initial_status, null=True)
    size = models.ForeignKey(to=s_models.Size, related_name="projects", on_delete=models.PROTECT, null=True)
    region = models.ForeignKey(to=s_models.Region, related_name="projects", on_delete=models.PROTECT, null=True)
    district = models.ForeignKey(to=s_models.District, related_name="projects", on_delete=models.PROTECT, null=True)
    town = UpperCaseCharField(max_length=40, null=True)
    duration = models.DecimalField(decimal_places=2, max_digits=10, default=1, verbose_name=('Duration (Years)'))
    authority = models.ForeignKey(to=s_models.Authority, related_name="projects", on_delete=models.PROTECT, null=True)
    remarks = models.CharField(max_length=1000, null=True, blank=True)
    quantity_demanded = models.DecimalField(decimal_places=2, max_digits=10, default=0, verbose_name=('Quantity Demanded (Tons)'))
    quantity_supplied = models.DecimalField(decimal_places=2, max_digits=10, default=0, verbose_name=('Quantity Supplied (Tons)'))
    latitude = models.DecimalField(decimal_places=20, max_digits=30, null=True, blank=True, verbose_name=('Latitude'))
    longitude = models.DecimalField(decimal_places=20, max_digits=30, null=True, blank=True, verbose_name=('Longitude'))
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(to=User, related_name="created_projects", on_delete=models.PROTECT, null=True)
    updated_by = models.ForeignKey(to=User, related_name="updated_projects", on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['-date_created']

    def get_coordinates(self):
        if self.latitude == None or self.longitude == None:
            return 'Not set'
        return f'({self.longitude:.4f}, {self.latitude:.4f})'

    def get_time_remaining(self):
        if self.start_date == None:
            return None
        return self.duration - ((date.today() - self.start_date).days) / decimal.Decimal(364.25)

    def get_location(self):
        return f'{self.region}, {self.district}, {self.town}'

    def get_balance(self):
        return self.quantity_demanded - self.quantity_supplied

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects-detail', kwargs={'pk': self.pk})


class ProjectImage(models.Model):
    project = models.ForeignKey(to=Project, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_pics')
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.project.name} - {self.image.name}'

    def save(self, *args, **kwargs):
        super(ProjectImage, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        print('Image', self.image.path)
        if img.height > 480 or img.width > 640:
            output_size = (640, 480)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('projects-detail', kwargs={'pk': self.project.id})


class ProjectContractor(models.Model):
    project = models.ForeignKey(to=Project, related_name="contractors", on_delete=models.CASCADE)
    contractor = models.ForeignKey(to=s_models.Contractor, related_name="projects", on_delete=models.PROTECT)
    sub_contractor = models.BooleanField(default=False)

    class Meta:
        unique_together = [['project', 'contractor']]

    def __str__(self):
        return self.contractor.name

    def get_absolute_url(self):
        return reverse('projects-detail', kwargs={'pk': self.project.id})

    def is_main(self):
        return not self.sub_contractor


class ProjectClient(models.Model):
    project = models.ForeignKey(to=Project, related_name="clients", on_delete=models.CASCADE)
    client = models.ForeignKey(to=s_models.Client, related_name="projects", on_delete=models.PROTECT)

    class Meta:
        unique_together = [['project', 'client']]

    def __str__(self):
        return self.client.name

    def get_absolute_url(self):
        return reverse('projects-detail', kwargs={'pk': self.project.id})


class ProjectFinancer(models.Model):
    project = models.ForeignKey(to=Project, related_name="financers", on_delete=models.CASCADE)
    financer = models.ForeignKey(to=s_models.Financer, related_name="projects", on_delete=models.PROTECT)

    class Meta:
        unique_together = [['project', 'financer']]

    def get_absolute_url(self):
        return reverse('projects-detail', kwargs={'pk': self.project.id})


class ProjectConsultant(models.Model):
    project = models.ForeignKey(to=Project, related_name="consultants", on_delete=models.CASCADE)
    consultant = models.ForeignKey(to=s_models.Consultant, related_name="projects", on_delete=models.PROTECT)

    class Meta:
        unique_together = [['project', 'consultant']]

    def get_absolute_url(self):
        return reverse('projects-detail', kwargs={'pk': self.project.id})


class ProjectSupplier(models.Model):
    project = models.ForeignKey(to=Project, related_name="suppliers", on_delete=models.CASCADE)
    supplier = models.ForeignKey(to=s_models.Supplier, related_name="projects", on_delete=models.PROTECT)
    # supplier = UpperCaseCharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=1, verbose_name=('Price/t VAT excl. (TZS)'))
    quantity = models.DecimalField(decimal_places=2, max_digits=10, default=0, verbose_name=('Quantity(Tons)'))
    brand = models.ForeignKey(to=s_models.Brand, related_name="suppliers", on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        unique_together = [['project', 'brand']]

    def __str__(self):
        return self.supplier.name

    def get_absolute_url(self):
        return reverse('projects-detail', kwargs={'pk': self.project.id})


class ProjectAudit(models.Model):
    project = models.ForeignKey(to=Project, related_name="audits", on_delete=models.CASCADE)
    remarks = models.CharField(max_length=1000, null=True, blank=True)
    demanded = models.DecimalField(decimal_places=2, max_digits=10, default=0, null=True)
    supplied = models.DecimalField(decimal_places=2, max_digits=10, default=0, null=True)
    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0, null=True)
    other = models.CharField(max_length=1000, null=True, blank=True)
    logged_by = models.ForeignKey(to=User, related_name="audits", on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    manual = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']

    def get_absolute_url(self):
        return reverse('projects-detail', kwargs={'pk': self.project.id})
