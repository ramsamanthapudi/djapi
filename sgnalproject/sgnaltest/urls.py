from django.urls import path, include
from .models import Student, Attendance
from .views import ViewSetClass

urlpatterns = [
    path('student/', ViewSetClass.as_view({'get':'list'}))]
