# Generated by Django 2.2.7 on 2021-05-27 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0025_auto_20210527_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsupplier',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='distributors', to='setups.Brand'),
        ),
    ]
