from django.db import models


class Employee(models.Model):
    roll_number = models.CharField( max_length=30, default=None,unique=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class Attendance(models.Model):
    date = models.DateField(primary_key=True)
    employee = models.ManyToManyField(Employee)


class Leave(models.Model):
    date = models.DateField(primary_key=True)
    employee = models.ManyToManyField(Employee)


class Break(models.Model):
    date = models.DateField(default=None)
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, default=None)
    employee = models.ManyToManyField(Employee)





