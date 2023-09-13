from django.urls import path
from . import views

urlpatterns = [
    #/playground/hello/ - url
    path('hello/', views.say_hello) # always add '/' at the end
]