# Generated by Django 2.2.7 on 2020-01-06 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popinfo', '0003_auto_20200106_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='win',
            old_name='winner_name',
            new_name='winner',
        ),
    ]
