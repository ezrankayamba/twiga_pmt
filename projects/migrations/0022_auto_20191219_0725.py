# Generated by Django 2.2.7 on 2019-12-19 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20191217_1346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date_created']},
        ),
    ]