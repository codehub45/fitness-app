# Generated by Django 4.2.22 on 2025-06-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0008_rename_classes_id_slots_classes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='date_time',
            field=models.DateField(),
        ),
    ]
