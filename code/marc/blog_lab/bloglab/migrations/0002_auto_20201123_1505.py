# Generated by Django 3.1.3 on 2020-11-23 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloglab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ragepage',
            name='photo',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='ragepage',
            name='caption',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='ragepage',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
