# Generated by Django 3.1.3 on 2020-11-18 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortner_app', '0004_auto_20201118_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlcode',
            name='url_counter',
            field=models.IntegerField(),
        ),
    ]
