# Generated by Django 4.2.5 on 2023-09-21 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0004_alter_dentalrecord_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentalrecord',
            name='date',
            field=models.DateField(),
        ),
    ]