# Generated by Django 3.2 on 2021-05-23 06:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wardhacovidhelpapp', '0015_vaccineavailablity'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccineavailablity',
            name='LastUpdated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
