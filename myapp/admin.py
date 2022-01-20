from django.contrib import admin
from myapp.models import Employee, Attendance, Break, Leave

admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Break)
admin.site.register(Leave)
