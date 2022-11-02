from django.db import models
from project.timestamps import TimestampsModel
from project.softDeletion import SoftDeletionModel

class Company(SoftDeletionModel, TimestampsModel):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=1200, blank=True, null=True)
    rut = models.CharField(max_length=16, unique=True)
    phone = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f'{self.rut}: {self.name}'

    class Meta:
        verbose_name_plural = "companies"


class Employee(SoftDeletionModel, TimestampsModel):
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    rut = models.CharField(max_length=16, unique=True)
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.rut}: {self.firstname} {self.lastname}'

    class Meta:
        verbose_name_plural = "employees"




