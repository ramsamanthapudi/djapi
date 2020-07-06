from rest_framework.serializers import ModelSerializer
from .models import Student, Attendance


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'