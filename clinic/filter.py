from django_filters import FilterSet
from .models import Patient

class PatientFilter(FilterSet):
    class Meta:
        model = Patient
        fields = {
            'package_id': ['exact'],
            'balance': ['gt', 'lt']
        }

