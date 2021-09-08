from django.db import models

# Create your models here.
class Department(models.Model):
    DepartmentId = models.AutoField(primary_key = True)
    DepartmentName = models.CharField(max_length = 500)

class Employee(models.Model):
   EmployeeId = models.AutoField(primary_key = True)
   EmployeeName = models.CharField(max_length = 500)
   Employeedept = models.CharField(max_length = 500)
   Employeejoin = models.DateField()
   Employeephoto = models.CharField(max_length = 500)
