# Generated by Django 3.1.3 on 2020-11-24 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squawker', '0003_auto_20201123_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squeek',
            name='photo',
        ),
    ]