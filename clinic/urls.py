from django.urls import path
from . import views

urlpatterns = [
    #/playground/hello/ - url
    path('package/', views.package_list), # always add '/' at the end
    path('package/<int:id>/', views.package_details), # always add '/' at the end
    path('patient/', views.patient_list),
    path('patient/<int:id>/', views.patient_details),
]