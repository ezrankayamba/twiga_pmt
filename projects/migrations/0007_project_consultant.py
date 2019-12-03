# Generated by Django 2.2.7 on 2019-12-02 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0004_auto_20191202_1821'),
        ('projects', '0006_auto_20191202_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='consultant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='setups.Consultant'),
        ),
    ]
