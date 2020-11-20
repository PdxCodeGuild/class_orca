# Generated by Django 2.2.4 on 2020-11-17 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_text', models.CharField(max_length=200)),
                ('short_code', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('code_assigned', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='LongURL',
        ),
    ]