# Generated by Django 5.0.1 on 2024-10-07 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_cameraconfiguration_camera_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cameraconfiguration',
            name='success_sound_path',
        ),
    ]
