# Generated by Django 3.1.3 on 2020-11-21 01:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chirp_posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chirpposts',
            name='edited_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='chirpposts',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chirpposts',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
