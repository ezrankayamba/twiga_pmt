from django.db import models
from django.db import models


class UpperCaseCharField(models.CharField):

    def __init__(self, *args, **kwargs):
        super(UpperCaseCharField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname, None)
        if value:
            value = value.upper()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(UpperCaseCharField, self).pre_save(model_instance, add)


class Config(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
