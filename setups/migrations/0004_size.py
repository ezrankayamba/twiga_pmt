# Generated by Django 2.2.7 on 2019-12-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0003_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4, unique=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
    ]
