from django.contrib import admin
from . import models

admin.site.register(models.Project)
admin.site.register(models.ProjectSupplier)
admin.site.register(models.ProjectContractor)
admin.site.register(models.ProjectFinancer)
admin.site.register(models.ProjectConsultant)
admin.site.register(models.ProjectAudit)
