# Generated by Django 3.1.3 on 2020-11-16 22:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list_app', '0002_auto_20201116_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 16, 22, 4, 21, 914512, tzinfo=utc)),
        ),
    ]