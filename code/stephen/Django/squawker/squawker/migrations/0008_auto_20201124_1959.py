# Generated by Django 3.1.3 on 2020-11-25 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squawker', '0007_auto_20201124_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squeek',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
