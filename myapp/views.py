from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee,Leave,Break,Attendance
from myapp.seralizer import EmployeeSerializer,LeaveSerializer,BreakSerializer,AttendanceSerializer


class EmployeeApi(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class LeaveApi(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer


class BreakApi(viewsets.ModelViewSet):
    queryset = Break.objects.all()
    serializer_class = BreakSerializer


class AttendanceApi(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
