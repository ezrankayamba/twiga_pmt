# Generated by Django 2.2.7 on 2021-06-05 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0012_client'),
        ('projects', '0034_auto_20210604_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='client',
        ),
        migrations.CreateModel(
            name='ProjectClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='setups.Client')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='projects.Project')),
            ],
            options={
                'unique_together': {('project', 'client')},
            },
        ),
    ]
