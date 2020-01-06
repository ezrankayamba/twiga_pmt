# Generated by Django 2.2.7 on 2020-01-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200103_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roleprivilege',
            name='privilege',
            field=models.CharField(choices=[('projects.create', 'Project - Create'), ('projects.edit', 'Project - Edit'), ('projects.delete', 'Project - Delete'), ('view.dashboard', 'View Dashboard'), ('view.map', 'View Map'), ('view.projects', 'View Projects'), ('view.setups', 'View Setups'), ('view.users', 'View Users'), ('view.roles', 'View Roles')], max_length=40),
        ),
    ]