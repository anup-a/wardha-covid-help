# Generated by Django 3.2 on 2021-05-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardhacovidhelpapp', '0008_teammembers'),
    ]

    operations = [
        migrations.AddField(
            model_name='plasmarequest',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
