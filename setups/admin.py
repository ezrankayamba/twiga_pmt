from django.contrib import admin
from . import models

admin.site.register(models.Status)
admin.site.register(models.Type)
admin.site.register(models.Contractor)
admin.site.register(models.Consultant)
admin.site.register(models.Supplier)
admin.site.register(models.Financer)
