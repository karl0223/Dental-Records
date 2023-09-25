
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from clinic.filter import PatientFilter
from clinic.models import Branch, DentalRecord, Dentist, Package, Patient, PaymentRecord, Procedure, Review
from .serializers import BranchSerializer, DentalRecordSerializer, DentistSerializer, PackageSerializer, PatientSerializer, PaymentRecordSerializer, ProcedureSerializer, ReviewSerializer


class PackageViewSet(ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    
class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]    # Generic Filtering
    filterset_class = PatientFilter
    search_fields = ['first_name', 'last_name']
    
class BranchViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    # filter each branch reviews 
    def get_queryset(self):
        return Review.objects.filter(branch_id=self.kwargs['branch_pk']) # returns the specific branch to post a review

    # context - to give additional information in the serializer
    def get_serializer_context(self):
        return { 'branch_id': self.kwargs['branch_pk']}
    

class DentistViewSet(ModelViewSet):
    queryset = Dentist.objects.all()
    serializer_class = DentistSerializer


class ProcedureViewSet(ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer


class DentalRecordViewSet(ModelViewSet):
     queryset = DentalRecord.objects.all()
     serializer_class = DentalRecordSerializer


class PaymentRecordViewSet(ModelViewSet):
    queryset = PaymentRecord.objects.all()
    serializer_class = PaymentRecordSerializer
