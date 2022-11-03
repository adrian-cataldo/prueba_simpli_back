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
        queryset = self.queryset.all()

        company_id = self.request.query_params.get('company_id', None)
        if company_id:
            company = Company.objects.filter(id=company_id).first()
            queryset = queryset.filter(company=company)

        return queryset

