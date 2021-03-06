# Generated by Django 2.2.7 on 2021-06-04 05:16

import core.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_project_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=core.models.UpperCaseCharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=core.models.UpperCaseCharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='town',
            field=core.models.UpperCaseCharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='projectsupplier',
            name='supplier',
            field=core.models.UpperCaseCharField(blank=True, max_length=255, null=True),
        ),
    ]
