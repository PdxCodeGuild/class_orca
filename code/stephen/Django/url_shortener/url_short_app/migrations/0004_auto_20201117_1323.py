# Generated by Django 3.1.3 on 2020-11-17 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_short_app', '0003_auto_20201117_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='long_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
