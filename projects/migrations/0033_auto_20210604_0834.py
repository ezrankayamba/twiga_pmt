# Generated by Django 2.2.7 on 2021-06-04 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0032_projectsupplier_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsupplier',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Price/t VAT excl. (TZS)'),
        ),
    ]
