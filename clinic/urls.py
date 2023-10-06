from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('packages', views.PackageViewSet) # endpoint - views
router.register('patients', views.PatientViewSet, basename='patients')
router.register('dentists', views.DentistViewSet)
router.register('branches', views.BranchViewSet)
router.register('procedures', views.ProcedureViewSet)
router.register('dentalrecords', views.DentalRecordViewSet)
router.register('paymentrecords', views.PaymentRecordViewSet)
router.register('appointments', views.AppointmentViewSet)

branches_router = routers.NestedDefaultRouter(router, 'branches', lookup='branch') # parent router - parent prefix - lookup parameters (branch_pk)
branches_router.register('reviews', views.ReviewViewSet, basename='branch-reviews') # branch-reviews-list / branch-reviews-detail

patient_router = routers.NestedDefaultRouter(router, 'patients', lookup='patient')
patient_router.register('images', views.PatientProfileImageViewSet, basename='patient-images')

urlpatterns = router.urls + branches_router.urls + patient_router.urls