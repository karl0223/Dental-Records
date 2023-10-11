from django.urls import path
from . import views

urlpatterns = [
    #/playground/hello/ - url
    path('hello/', views.HelloView.as_view()) # always add '/' at the end
]