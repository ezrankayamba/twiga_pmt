# Generated by Django 2.2.7 on 2021-05-27 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_auto_20210527_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectsupplier',
            old_name='under',
            new_name='brand',
        ),
    ]
