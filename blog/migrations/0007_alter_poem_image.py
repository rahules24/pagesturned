# Generated by Django 4.1.2 on 2022-11-20 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_poem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='image',
            field=models.ImageField(default='', upload_to='blog/images'),
        ),
    ]
