# Generated by Django 2.2.4 on 2020-11-17 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LongURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_text', models.CharField(max_length=200)),
                ('short_code', models.CharField(max_length=20)),
            ],
        ),
    ]
