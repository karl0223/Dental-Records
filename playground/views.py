from django.shortcuts import render
from .tasks import notify_customer
# Create your views here.

def say_hello(request):
    notify_customer.delay('Hello')
   
    return render(request, 'hello.html', { 'name' : 'Karl'})
