
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from clinic.filter import PatientFilter
from clinic.models import Appointment, Branch, DentalRecord, Dentist, Package, Patient, PaymentRecord, Procedure, Review
from clinic.pagination import DefaultPagination
from clinic.permissions import IsAdminOrReadOnly
from .serializers import AppointmentSerializer, BranchSerializer, DentalRecordSerializer, DentistSerializer, PackageSerializer, PatientSerializer, PaymentRecordSerializer, ProcedureSerializer, ReviewSerializer


class PackageViewSet(ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_serializer_context(self):
        return {'request': self.request}
    
class PatientViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]    # Generic Filtering
    filterset_class = PatientFilter
    pagination_class = DefaultPagination
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['balance', 'registration_date']
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        (patient, created) = Patient.objects.get_or_create(user_id=request.user.id)        # use get or create to not return an error, returns (tuple)
        if request.method == 'GET':
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = PatientSerializer(patient, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    
class BranchViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminOrReadOnly]

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    # filter each branch reviews 
    def get_queryset(self):
        return Review.objects.filter(branch_id=self.kwargs['branch_pk']) # returns the specific branch to post a review

    # context - to give additional information in the serializer
    def get_serializer_context(self):
        return { 'branch_id': self.kwargs['branch_pk']}
    

class DentistViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
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

class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

