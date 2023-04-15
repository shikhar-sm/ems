from django.db import models
from django.core.validators import MinLengthValidator

class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150,null=False)
    
class Employee(models.Model):
    id = models.CharField(primary_key=True,max_length=5,validators=[MinLengthValidator(5)])
    name = models.CharField(max_length=200)
    is_manager = models.BooleanField(default=False)
    manager = models.ForeignKey('Employee',on_delete=models.SET_NULL,null=True)
    department = models.ForeignKey(Department,on_delete=models.PROTECT)
    role = models.CharField(max_length=100)
