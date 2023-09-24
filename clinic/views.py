from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from clinic.models import Package, Patient
from .serializers import PackageSerializer, PatientSerializer


class PackageViewSet(ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}
    
    def delete(self, request, pk):
        package = get_object_or_404(Package, pk=pk)
        package.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def delete(self, request, id):
        patient = get_object_or_404(Patient, pk=id)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)