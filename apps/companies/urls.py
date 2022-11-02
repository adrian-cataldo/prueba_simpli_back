from django.urls import path
from apps.companies import views
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet, basename='companies')
router.register(r'employees', views.EmployeesViewSet, basename='employees')

urlpatterns = [
    path('', include(router.urls)),
]
