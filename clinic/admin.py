from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'package_type', 'price']
    list_editable = ['price']
    list_per_page = 10 # simple pagination

@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'branch']
    list_editable = ['branch']
    ordering = ['first_name', 'last_name']
    list_per_page = 10

@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    list_per_page = 10

@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'city']
    ordering = ['street', 'city']
    list_per_page = 10