# Generated by Django 3.2 on 2021-05-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardhacovidhelpapp', '0012_covidnewspost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='covidnewspost',
            name='Full_Description',
        ),
        migrations.AddField(
            model_name='covidnewspost',
            name='Paragraph_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='covidnewspost',
            name='Paragraph_10',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='covidnewspost',
            name='Paragraph_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='covidnewspost',
            name='Paragraph_3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='covidnewspost',
            name='Paragraph_4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='covidnewspost',
            name='Paragraph_5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='covidnewspost',
            name='Paragraph_6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='covidnewspost',
            name='Paragraph_7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='covidnewspost',
            name='Paragraph_8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='covidnewspost',
            name='Paragraph_9',
            field=models.TextField(blank=True, null=True),
        ),
    ]
