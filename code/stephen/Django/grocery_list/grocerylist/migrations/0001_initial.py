# Generated by Django 3.1.3 on 2020-11-13 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grocerylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listitem', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField()),
                ('completed_date', models.DateTimeField()),
                ('completed_boolean', models.BooleanField(default=False)),
            ],
        ),
    ]
