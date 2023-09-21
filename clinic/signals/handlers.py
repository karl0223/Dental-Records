from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from clinic.models import Patient, PaymentRecord


@receiver(post_save, sender=PaymentRecord)
def update_patient_balance(sender, instance, **kwargs):
    # Calculate the patient's balance based on the latest payment records
    latest_payment_record = instance.patient.payment_records.last()
    if latest_payment_record:
        instance.patient.balance = latest_payment_record.balance
    else:
        instance.patient.balance = instance.patient.package.price if instance.patient.package else 0
    instance.patient.save()
