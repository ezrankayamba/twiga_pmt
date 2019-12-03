from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Authority(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=40, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.name


class Contractor(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=40, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.name


class Financer(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=40, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.name


class Consultant(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=40, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=40, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.name
