from django.urls import path
from . import views

urlpatterns = [
    #/playground/hello/ - url
    path('package/', views.PackageList.as_view()), # always add '/' at the end
    path('package/<int:pk>/', views.PackageDetail.as_view()), # always add '/' at the end
    path('patient/', views.PatientList.as_view()),
    path('patient/<int:id>/', views.PatientDetail.as_view()),
]