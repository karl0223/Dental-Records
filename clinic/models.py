from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    
class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, primary_key=True)

class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

class Dentist(models.Model):
    GENERAL_DENTIST = 'GD'
    PEDIATRIC_DENTIST = 'PD'
    ORTHODENTIST = 'OD'
    GUM_SPECIALIST = 'GS'
    ROOT_CANAL_SPECIALIST = 'RCS'
    ORAL_SURGEON = 'OS'
    PROSTHODONTIST = 'PTD'
    DENTIST_ROLE_CHOICES = [
        (GENERAL_DENTIST, "General Dentist"),
        (PEDIATRIC_DENTIST, ' Pediatric Dentist'),
        (ORTHODENTIST, 'Orthodentist'),
        (GUM_SPECIALIST, 'Gum Specialist'),
        (ROOT_CANAL_SPECIALIST, 'Root Canal Specialist'),
        (ORAL_SURGEON, 'Oral Surgeon'),
        (PROSTHODONTIST, 'Prothodontist'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    role = models.CharField(max_length=5, choices=DENTIST_ROLE_CHOICES, default=GENERAL_DENTIST)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)


class Package(models.Model):
    PACKAGE_A = 'A'
    PACKAGE_B = 'B'
    PACKAGE_C = 'C'
    PACKAGE_CHOICES = [
        (PACKAGE_A, 'Standard'),
        (PACKAGE_B, 'Premium'),
        (PACKAGE_C, 'Delux'),
    ]
    title = models.CharField(max_length=255)
    package_type = models.CharField(max_length=1, choices=PACKAGE_CHOICES, default=PACKAGE_A)
    price= models.DecimalField(max_digits=10, decimal_places=2)

class Procedure(models.Model):
    subjective = models.TextField()
    objective = models.TextField()
    assessment = models.TextField()
    plan = models.TextField()

class DentalRecord(models.Model):
    date = models.DateTimeField(auto_now=True)
    patient = models.OneToOneField(Patient, on_delete=models.PROTECT, primary_key=True)
    dentist = models.ForeignKey(Dentist, on_delete=models.PROTECT)
    procedure = models.ForeignKey(Procedure, on_delete=models.PROTECT)

class PaymentRecord(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.PROTECT, primary_key=True)
    package = models.ForeignKey(Package, on_delete=models.PROTECT)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    last_update = models.DateTimeField(auto_now=True)



