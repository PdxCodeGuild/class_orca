# Generated by Django 2.2.4 on 2020-11-13 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_app', '0003_remove_groceryitem_date_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceryitem',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
