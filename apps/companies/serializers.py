from .models import Company, Employee
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('__all__')

class EmployeeSerializer(serializers.ModelSerializer):
    company_id = serializers.IntegerField()
    company = CompanySerializer(read_only=True, many=False)

    class Meta:
        model = Employee
        fields = ('__all__')

