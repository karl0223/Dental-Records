from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from clinic.models import Package
from .serializers import PackageSerializer

# Create your views here.
@api_view()
def package_list(request):
    return Response('ok')

@api_view()
def package_details(request, id):
    package = Package.objects.get(pk=id)
    serializer = PackageSerializer(package)
    return Response(serializer.data)

