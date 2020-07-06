from django.db import models
from django.db.models.signals import post_save, pre_save


# Create your models here.

class Student(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=40)
    Age = models.IntegerField()

    def __str__(self):
        return self.Name


class Attendance(models.Model):
    student_record = models.OneToOneField(Student, on_delete=models.CASCADE)
    Attendance_percentage = models.FloatField(default=75)

    def __str__(self):
        return self.student_record.Name


def save_post(sender, instance, created, **kwargs):
    if created:
        Attendance.objects.create(student_record=instance)


post_save.connect(receiver=save_post, sender=Student)
