from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=40)
    price = models.FloatField()
    # access = models.ForeignKey(User,
    #                            on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

