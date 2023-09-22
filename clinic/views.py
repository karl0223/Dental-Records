from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from clinic.models import Package, Patient
from .serializers import PackageSerializer, PatientSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def package_list(request):
    if request.method == "GET":
        queryset = Package.objects.all()
        serializer = PackageSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PackageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        return Response('ok')

@api_view()
def package_details(request, id):
    package = get_object_or_404(Package, pk=id)
    serializer = PackageSerializer(package)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def patient_list(request):
    queryset = Patient.objects.all()
    serializer = PatientSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def patient_details(request, id):
    patient = get_object_or_404(Patient, pk=id)
    serializer = PatientSerializer(patient)
    return Response(serializer.data)
