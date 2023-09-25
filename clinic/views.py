from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
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
