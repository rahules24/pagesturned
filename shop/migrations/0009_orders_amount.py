# Generated by Django 4.1.2 on 2022-11-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_delete_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0, max_length=7),
        ),
    ]
