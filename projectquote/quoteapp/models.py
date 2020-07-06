from django.db import models

# Create your models here.

class Quote(models.Model):
    author = models.CharField(max_length=40)
    body = models.TextField()
    context = models.CharField(max_length=200, blank=True)
    source = models.CharField(max_length=47, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author