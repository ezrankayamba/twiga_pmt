# Generated by Django 2.2.7 on 2019-12-09 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0004_size'),
        ('projects', '0016_auto_20191209_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='setups.Size'),
        ),
    ]
