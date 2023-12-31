# Generated by Django 4.2.5 on 2023-09-30 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_alter_patient_options_remove_dentist_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
                ('dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.dentist')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.patient')),
            ],
            options={
                'permissions': [('cancel_appointment', 'Can cancel appointment')],
            },
        ),
    ]
