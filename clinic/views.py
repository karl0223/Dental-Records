
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from clinic.filter import PatientFilter
from clinic.models import Appointment, Branch, DentalRecord, Dentist, Package, Patient, PatientProfileImage, PaymentRecord, Procedure, Review
from clinic.pagination import DefaultPagination
from clinic.permissions import IsAdminOrReadOnly, ViewPatientHistoryPermission
from .serializers import AppointmentSerializer, BranchSerializer, CreateAppointmentSerializer, CreateDentalRecordSerializer, CreatePaymentRecordSerializer, DentalRecordSerializer, DentistSerializer, PackageSerializer, PatientProfileImageSerializer, PatientSerializer, PaymentRecordSerializer, ProcedureSerializer, ReviewSerializer


class PackageViewSet(ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_serializer_context(self):
        return {'request': self.request}
    
class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.prefetch_related('profile_image', 'user').all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]    # Generic Filtering
    filterset_class = PatientFilter
    pagination_class = DefaultPagination
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['balance', 'registration_date']
    permission_classes = [IsAdminUser]

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [AllowAny()]
    #     return [IsAuthenticated()]

    @action(detail=True, permission_classes=[ViewPatientHistoryPermission])
    def history(self, request, pk):
        return Response('ok')


    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (patient, created) = Patient.objects.prefetch_related('profile_image', 'user').get_or_create(user_id=request.user.id)        # use get or create to not return an error, returns (tuple)
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
    

class DentistViewSet(ModelViewSet):
    queryset = Dentist.objects.all()
    serializer_class = DentistSerializer
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (dentist, created) = Dentist.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = DentistSerializer(dentist)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = DentistSerializer(dentist, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class ProcedureViewSet(ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
    permission_classes = [IsAdminUser]


class DentalRecordViewSet(ModelViewSet):
     queryset = DentalRecord.objects.all()
     permission_classes = [IsAdminUser]

     def get_serializer_class(self):
         if self.request.method == 'POST':
             return CreateDentalRecordSerializer
         return DentalRecordSerializer
     
     @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
     def me(self, request):
        (patient, created) = Patient.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            dental_record = DentalRecord.objects.filter(patient=patient)
            serializer = DentalRecordSerializer(dental_record, many=True)
            return Response(serializer.data)
        
class PaymentRecordViewSet(ModelViewSet):
    queryset = PaymentRecord.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PaymentRecordSerializer
        return CreatePaymentRecordSerializer

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (patient, created) = Patient.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            payment_record = PaymentRecord.objects.filter(patient=patient)
            serializer = PaymentRecordSerializer(payment_record, many=True)
            return Response(serializer.data)

        

class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AppointmentSerializer
        return CreateAppointmentSerializer
    
    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (patient, created) = Patient.objects.get_or_create(user_id=request.user.id)
        appointment = Appointment.objects.filter(patient=patient)
        if request.method == 'GET':
            serializer = AppointmentSerializer(appointment, many=True)
            return Response(serializer.data)
        
class PatientProfileImageViewSet(ModelViewSet):
    serializer_class = PatientProfileImageSerializer

    def get_serializer_context(self):
        return {'patient_id': self.kwargs['patient_pk']}

    def get_queryset(self):
        return PatientProfileImage.objects.filter(patient_id=self.kwargs['patient_pk'])


