# Generated by Django 3.0.3 on 2023-06-04 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0002_task_lorat_temp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='lorat_temp',
            new_name='lora_temp',
        ),
    ]
