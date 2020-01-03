from django.db import models


class Config(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
