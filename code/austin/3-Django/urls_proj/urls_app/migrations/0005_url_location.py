# Generated by Django 2.2.4 on 2020-11-18 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls_app', '0004_url_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
