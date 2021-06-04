from uuid import uuid4

from django.db import models


# Create your models here.
class emplyefom(models.Model):
    emp_id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    emp_name = models.CharField(max_length=225)
    emp_mail = models.EmailField(max_length=225)
    emp_job = models.CharField(max_length=225)
    join_date = models.DateTimeField()

    def __str__(self):
        return self.emp_name


class Employee(models.Model):
    name = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    course = models.CharField(max
    _length=200)

    def __str__(self):
        return self.name
