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

branches_router = routers.NestedDefaultRouter(router, 'branches', lookup='branch') # parent router - parent prefix - lookup parameters (branch_pk)
branches_router.register('reviews', views.ReviewViewSet, basename='branch-reviews') # branch-reviews-list / branch-reviews-detail

urlpatterns = router.urls + branches_router.urls