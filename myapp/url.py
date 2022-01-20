from django.urls import path,include
import myapp.views as views
from rest_framework import routers
route = routers.DefaultRouter()
route.register('',views.EmployeeApi,basename='')

urlpatterns = [
    path('',include(route.urls)),

]
