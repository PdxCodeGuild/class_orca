# Generated by Django 3.1.3 on 2020-11-18 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortner_app', '0002_auto_20201117_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlcode',
            name='user_ip',
            field=models.CharField(default='0.0.0.0', max_length=200),
            preserve_default=False,
        ),
    ]