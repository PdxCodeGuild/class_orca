# Generated by Django 2.2.4 on 2020-11-13 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_app', '0002_auto_20201113_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groceryitem',
            name='date_completed',
        ),
    ]
