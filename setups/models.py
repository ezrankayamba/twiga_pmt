from django.db import models
from core.models import UpperCaseCharField

SETUPS_LIST = ['brand', 'authority', 'consultant', 'contractor', 'financer', 'supplier', 'size', 'status', 'region', 'district', 'type', 'client']


class Size(models.Model):
    code = UpperCaseCharField(max_length=4, unique=True)
    name = UpperCaseCharField(max_length=40)

    def __str__(self):
        return self.name


class Status(models.Model):
    code = UpperCaseCharField(max_length=4, unique=True)
    name = UpperCaseCharField(max_length=40)
    group = UpperCaseCharField(max_length=40, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Statuses"


class Type(models.Model):
    name = UpperCaseCharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = UpperCaseCharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = UpperCaseCharField(max_length=40)
    region = models.ForeignKey(to=Region, on_delete=models.CASCADE, related_name='districts')

    class Meta:
        unique_together = [['name', 'region']]

    def __str__(self):
        return self.name


class Authority(models.Model):
    name = UpperCaseCharField(max_length=100, unique=True)
    contact_person = models.CharField(max_length=40, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Authorities"

    def __str__(self):
        return self.name


class Client(models.Model):
    name = UpperCaseCharField(max_length=100, unique=True)
    contact_person = models.CharField(max_length=40, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.name


class Contractor(models.Model):
    name = UpperCaseCharField(max_length=100, unique=True)
    contact_person = models.CharField(max_length=40, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.name


class Financer(models.Model):
    name = UpperCaseCharField(max_length=100, unique=True)
    contact_person = models.CharField(max_length=40, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.name


class Consultant(models.Model):
    name = UpperCaseCharField(max_length=100, unique=True)
    contact_person = models.CharField(max_length=40, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = UpperCaseCharField(max_length=100, unique=True)
    contact_person = models.CharField(max_length=40, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = UpperCaseCharField(max_length=100, unique=True)
    contact_person = models.CharField(max_length=40, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.name
