from django.shortcuts import render
from .tasks import notify_customers
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import requests
import logging

logger = logging.getLogger(__name__)     # playground.views

# Create your views here.

class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received Response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('Httpbin is offline')
        return render(request, 'hello.html', { 'name' : data})

