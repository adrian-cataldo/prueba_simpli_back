from rest_framework import viewsets
from .models import Company, Employee
from.serializers import CompanySerializer, EmployeeSerializer
from project.SoftDeleteViewSet import SoftDeleteViewSet

class CompanyViewSet(viewsets.ModelViewSet, SoftDeleteViewSet):
    queryset = Company.objects.all().order_by('-id')
    serializer_class = CompanySerializer
    querysetTrashed = Company.all_objects.all().dead().order_by('-id')


class EmployeesViewSet(viewsets.ModelViewSet, SoftDeleteViewSet):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer
    querysetTrashed = Employee.all_objects.all().dead().order_by('-id')

    def get_queryset(self):
        queryset = self.queryset

        company = self.request.query_params.get('company', None)
        if company:
            queryset = queryset.filter(company__rut=company)

        return queryset