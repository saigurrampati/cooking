# Generated by Django 3.1.7 on 2021-04-30 11:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipes_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='images',
            field=models.ImageField(default=datetime.datetime(2021, 4, 30, 11, 45, 31, 472146, tzinfo=utc), upload_to='media/'),
        ),
    ]
