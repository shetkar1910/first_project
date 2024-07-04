from django.db import models
from django.utils import timezone

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_num = models.IntegerField(unique=True)
    designation = models.CharField(max_length=100)
    salary = models.IntegerField()
    date_joined = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.salary}"
    
    def __repr__(self):
        return str(self)

    class Meta:
        db_table = "employee"  # app_employee
