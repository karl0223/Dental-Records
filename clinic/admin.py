from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'package_type', 'price']
    list_per_page = 10 # simple pagination
    search_fields = ['title__istartswith']

@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'branch_name', 'package_type']
    # list_editable = ['branch_name']
    ordering = ['first_name', 'last_name']
    list_per_page = 10
    list_select_related = ['branch', 'package']

    def branch_name(self, patient):
        return patient.branch.name
    
    def package_type(self, patient):
        return patient.package.title
    
@admin.register(models.Dentist)
class DentistAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'role']
    ordering = ['first_name', 'last_name']
    list_per_page = 10


@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    list_per_page = 10

@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['branch', 'street', 'city']
    ordering = ['street', 'city']
    list_per_page = 10
    list_select_related = ['branch']

    def branch(self, address):
        return address.branch.name

@admin.register(models.PaymentRecord)
class PaymentRecordAdmin(admin.ModelAdmin):
    readonly_fields = ['balance']
    list_display = ['patient', 'display_package', 'display_package_price','balance', 'payment_details', 'amount', 'last_update']
    ordering = ['last_update']
    list_per_page = 10


    def display_package(self, obj):
        return obj.patient.package.title if obj.patient.package else None

    def display_package_price(self, obj):
        return obj.patient.package.price if obj.patient.package else None

    display_package.short_description = 'Package'

    display_package_price.short_description = 'Package Price'
        
