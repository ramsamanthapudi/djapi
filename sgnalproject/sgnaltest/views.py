from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Student, Attendance
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ViewSetClass(ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
