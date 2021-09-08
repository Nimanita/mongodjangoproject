from rest_framework import serializers
from employeeapp.models import Employee,Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields =('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields =('EmployeeId','EmployeeName','Employeedept','Employeejoin','Employeephoto')