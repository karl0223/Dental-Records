# Generated by Django 4.2.5 on 2023-10-03 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0005_alter_appointment_end_time_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can view history')]},
        ),
    ]
