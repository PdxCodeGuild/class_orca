# Generated by Django 3.1.3 on 2020-11-18 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_link', models.TextField()),
                ('short_url', models.CharField(max_length=5)),
            ],
        ),
    ]
