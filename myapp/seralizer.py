from rest_framework import serializers
from myapp.models import Employee,Attendance,Break,Leave


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class BreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Break
        fields = "__all__"


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = "__all__"