# Generated by Django 2.2.7 on 2019-12-09 12:29

from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20191209_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.ForeignKey(default=projects.models.initial_status, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='setups.Status'),
        ),
    ]