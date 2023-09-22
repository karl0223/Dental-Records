from decimal import Decimal
from rest_framework import serializers

from clinic.models import Package, Patient

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['title', 'package_type', 'price', 'price_with_discount']


    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # package_type = serializers.CharField(max_length=1)
    # package_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price')
    price_with_discount = serializers.SerializerMethodField(method_name='calculate_discount')

    def calculate_discount(self, package):
        return package.price - (package.price * Decimal(.10))
    
    def create(self, validated_data):
        package = Package(**validated_data)
        package.other = 1
        package.save()
        return package
    
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'phone', 'registration_date', 'branch', 'package']