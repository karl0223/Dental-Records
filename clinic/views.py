from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view()
def package_list(request):
    return Response('ok')

@api_view()
def package_details(request, id):
    return Response(id)

