# Generated by Django 4.1.2 on 2022-11-12 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_poem_comments_alter_poem_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='comments',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='poem',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
