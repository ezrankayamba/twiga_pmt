# Generated by Django 2.2.7 on 2019-11-30 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0001_initial'),
        ('projects', '0002_auto_20191130_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='minicipal',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='setups.Region'),
        ),
        migrations.AddField(
            model_name='project',
            name='town',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
