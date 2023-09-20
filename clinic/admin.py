from typing import Any
from django.contrib import admin, messages
from django.db.models.query import QuerySet
from . import models

# Register your models here.

class PackageFilter(admin.SimpleListFilter):
    title = 'Package Price'
    parameter_name = 'package_price'

    def lookups(self, request, model_admin):
        return [
            ('<50k', 'Mid')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<50k':
            return queryset.filter(price__lt=50000)

@admin.register(models.Package)
class PackageAdmin(admin.ModelAdmin):
    actions = ['price_50k']
    list_display = ['title', 'package_type', 'price']
    list_per_page = 10 # simple pagination
    search_fields = ['title__istartswith']
    list_filter = [PackageFilter]

    @admin.action(description='Change price to 50k')
    def price_50k(self, request, queryset):
        updated_price = queryset.update(price=50000)
        self.message_user(request, f'{updated_price} package were successfully updated.', messages.ERROR)


@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'branch_name', 'package_type']
    # list_editable = ['branch_name']
    ordering = ['first_name', 'last_name']
    list_per_page = 10
    list_select_related = ['branch', 'package']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    def branch_name(self, patient):
        return patient.branch.name
    
    def package_type(self, patient):
        return patient.package.title
    
@admin.register(models.Dentist)
class DentistAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'role']
    ordering = ['first_name', 'last_name']
    list_per_page = 10
    search_fields = ['first_name__istartswith', 'last_name__istartswith']


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
    autocomplete_fields = ['patient']
    readonly_fields = ['balance']
    list_display = ['patient', 'display_package', 'display_package_price','balance', 'payment_details', 'amount', 'last_update']
    ordering = ['last_update']
    list_per_page = 10
    list_filter = ['last_update']


    def display_package(self, obj):
        return obj.patient.package.title if obj.patient.package else None

    def display_package_price(self, obj):
        return obj.patient.package.price if obj.patient.package else None

    display_package.short_description = 'Package'

    display_package_price.short_description = 'Package Price'

@admin.register(models.DentalRecord)
class DentalRecordAdmin(admin.ModelAdmin):
    autocomplete_fields = ['patient', 'dentist', 'procedure']
    list_display = ['patient', 'dentist', 'procedure', 'date']
    ordering = ['date']
    list_per_page = 10
    list_filter = ['date']
    list_select_related = ['patient', 'dentist', 'procedure']
    
        
@admin.register(models.Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'duration_minutes', 'cost']
    list_per_page = 10
    search_fields = ['name__istartswith']