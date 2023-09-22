from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from clinic.models import Package, Patient
from .serializers import PackageSerializer, PatientSerializer


class PackageList(APIView):
    def get(self, request):
        queryset = Package.objects.all()
        serializer = PackageSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PackageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

class PackageDetail(APIView):
    def get(self, request, id):
        package = get_object_or_404(Package, pk=id)
        serializer = PackageSerializer(package)
        return Response(serializer.data)
    
    def put(self, request, id):
        package = get_object_or_404(Package, pk=id)
        serializer = PackageSerializer(package, data=request.data) # Item - data
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        package = get_object_or_404(Package, pk=id)
        package.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
       
class PatientList(APIView):
    def get(self, request):
        queryset = Patient.objects.all()
        serializer = PatientSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PatientDetail(APIView):
    def get(self, request, id):
        patient = get_object_or_404(Patient, pk=id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    def put(self, request, id):
        patient = get_object_or_404(Patient, pk=id)
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        patient = get_object_or_404(Patient, pk=id)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)