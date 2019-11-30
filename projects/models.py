from django.db import models
from django.urls import reverse
from setups import models as s_models

PROJECT_STATUS_LIST = (('INT', "Initiated"), ('ONG', "Ongoing"), ('CMP', "Completed"))


class Type(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    type = models.ForeignKey(to=Type, related_name="projects", on_delete=models.PROTECT)
    status = models.CharField(max_length=10, default='INT')
    region = models.ForeignKey(to=s_models.Region, related_name="projects", on_delete=models.PROTECT, null=True)
    municipal = models.CharField(max_length=40, null=True)
    town = models.CharField(max_length=40, null=True)
    duration = models.DecimalField(decimal_places=2, max_digits=10, default=1, verbose_name=('Duration(Years)'))

    def get_status(self):
        for en in PROJECT_STATUS_LIST:
            if(en[0] == self.status):
                return en[1]
        return 'Unknown'

    def get_location(self):
        return f'{self.region}, {self.municipal}, {self.town}'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects-home', kwargs={})
