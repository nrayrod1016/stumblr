# Generated by Django 3.2.4 on 2021-09-07 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='post',
        ),
    ]