from django.db import models
import random

def generate_employee_id():
    return ''.join(random.choices('0123456789', k=7))

class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=10, choices=(('active', 'active'), ('inactive', 'inactive')))
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    employee_id = models.CharField(max_length=7, unique=True, default=generate_employee_id)

class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    role_name = models.CharField(default="null", max_length=100)
    date_of_joining = models.DateField()
    last_date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)