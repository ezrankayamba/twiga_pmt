# Generated by Django 2.2.7 on 2020-01-06 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('popinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Win',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('award_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popinfo.AwardSession')),
            ],
        ),
        migrations.AlterField(
            model_name='fact',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popinfo.Win'),
        ),
        migrations.DeleteModel(
            name='Winner',
        ),
    ]