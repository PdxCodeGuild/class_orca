# Generated by Django 3.1.3 on 2020-11-25 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chirp_posts', '0003_auto_20201123_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='chirpposts',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]