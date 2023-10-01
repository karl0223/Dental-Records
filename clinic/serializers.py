from decimal import Decimal
from rest_framework import serializers

from clinic.models import Appointment, Branch, DentalRecord, Dentist, Package, Patient, PaymentRecord, Procedure, Review

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id','title', 'package_type', 'price', 'price_with_discount']


    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # package_type = serializers.CharField(max_length=1)
    # package_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price')
    price_with_discount = serializers.SerializerMethodField(method_name='calculate_discount')

    def calculate_discount(self, package):
        return package.price - (package.price * Decimal(.10))
    
class PatientSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
        model = Patient
        fields = ['id', 'user_id', 'first_name', 'last_name', 'phone', 'registration_date', 'branch', 'package', 'current_balance']

    current_balance = serializers.SerializerMethodField(method_name='get_balance')

    def get_balance(self, patient):
        return patient.balance

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'date']

    # overwrite the create to automatically get the branch id  ---- no need to specify the branch id
    # overwrite the def get_serializer_context(self): to get the branch_id in the self.context['branch_id]
    def create(self, validated_data):
        branch_id = self.context['branch_id']
        return Review.objects.create(branch_id=branch_id, **validated_data)
    

class DentistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentist
        fields = ['id', 'user_id', 'first_name', 'last_name', 'phone', 'role']

class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ['id', 'name', 'code', 'description', 'duration_minutes', 'cost']

class SimplePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name']

class SimpleDentistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentist
        fields = ['id', 'user_id', 'first_name', 'last_name']
        
class SimpleProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ['id', 'name']

class DentalRecordSerializer(serializers.ModelSerializer):
    patient = SimplePatientSerializer()
    dentist = SimpleDentistSerializer()
    procedure = SimpleProcedureSerializer()
    class Meta:
        model = DentalRecord
        fields = ['id', 'patient', 'dentist', 'procedure', 'date']


class PaymentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRecord
        fields = ['id', 'patient', 'dental_record', 'payment_details', 'amount']


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'dentist', 'start_time', 'end_time']