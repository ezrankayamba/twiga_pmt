from django.db import models


class Size(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Status(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=40)
    region = models.ForeignKey(to=Region, on_delete=models.CASCADE, related_name='districts')

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
