# Generated by Django 4.2.22 on 2025-06-05 13:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0003_rename_class_name_slots_class_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slots',
            old_name='timings',
            new_name='end_timings',
        ),
        migrations.AddField(
            model_name='slots',
            name='start_timings',
            field=models.TimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
