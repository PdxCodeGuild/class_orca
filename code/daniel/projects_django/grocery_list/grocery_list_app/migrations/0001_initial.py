# Generated by Django 3.1.3 on 2020-11-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grocery_item', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField()),
                ('date_complete', models.DateTimeField()),
                ('item_complete', models.BooleanField(default=False)),
            ],
        ),
    ]
