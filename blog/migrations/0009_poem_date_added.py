# Generated by Django 4.1.2 on 2022-11-20 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_poem_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='date_added',
            field=models.DateField(default=datetime.date(2022, 11, 21)),
        ),
    ]
