# Generated by Django 3.1.3 on 2020-11-17 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_short_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='long_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shortener',
            name='short_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
