from django.db import models
from django.db.models.aggregates import Sum

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

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

    # Change the rendered package title in the admin
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        # Change the sort order by its title
        ordering = ['title', 'package_type', 'price']

class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='patients')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)

    def calculate_initial_balance(self):
        # Calculate the initial balance based on the assigned package and any outstanding balance
        package_balance = self.package.price if self.package else 0
        # outstanding_balance = self.payment_records.aggregate(models.Sum('amount'))['amount__sum'] or 0
        return package_balance

    def save(self, *args, **kwargs):
        # Calculate and set the current balance when saving the patient
        self.balance = self.calculate_initial_balance()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
   
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

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Procedure(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the procedure", default='')
    code = models.CharField(max_length=20, unique=True, help_text="Procedure code or identifier", default='')
    description = models.TextField(blank=True, help_text="Description of the procedure")
    duration_minutes = models.PositiveIntegerField(help_text="Duration of the procedure in minutes", default=0)
    cost = models.DecimalField(max_digits=10, decimal_places=2, help_text="Cost of the procedure", default=0)
    subjective = models.TextField(blank=True)
    objective = models.TextField(blank=True)
    assessment = models.TextField(blank=True)
    plan = models.TextField(blank=True)

    def __str__(self):
        return self.name

class DentalRecord(models.Model):
    date = models.DateTimeField(auto_now=True)
    patient = models.OneToOneField(Patient, on_delete=models.PROTECT, primary_key=True)
    dentist = models.ForeignKey(Dentist, on_delete=models.PROTECT)
    procedure = models.ForeignKey(Procedure, on_delete=models.PROTECT)

    def formatted_date(self):
        return self.date.strftime('%d-%m-%Y')  # Format as day-month-year

    def __str__(self):
        return f'{self.patient} - {self.formatted_date()}'

class PaymentRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='payment_records')
    payment_details = models.TextField(default="")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    last_update = models.DateTimeField(auto_now=True)
    dental_record = models.ForeignKey(DentalRecord, on_delete=models.PROTECT, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calculate the balance based on the previous balance and the new payment amount
        previous_balance = self.patient.balance if hasattr(self.patient, 'balance') else 0
        self.balance = previous_balance - self.amount

        super().save(*args, **kwargs)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE, null=True, blank=True)



