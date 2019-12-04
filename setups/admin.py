from django.contrib import admin
from . import models

admin.site.register(models.Type)
admin.site.register(models.Region)
admin.site.register(models.Authority)
admin.site.register(models.Contractor)
admin.site.register(models.Financer)
admin.site.register(models.Consultant)
admin.site.register(models.Supplier)
