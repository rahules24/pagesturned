# Generated by Django 4.1.2 on 2022-11-23 12:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_poem_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
