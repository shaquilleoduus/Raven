# Generated by Django 3.0.8 on 2020-07-23 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raven', '0002_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='location_name',
            new_name='name',
        ),
    ]