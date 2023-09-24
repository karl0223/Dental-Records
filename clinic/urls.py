from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('package', views.PackageViewSet) # endpoint - views
router.register('patient', views.PatientViewSet)

urlpatterns = router.urls