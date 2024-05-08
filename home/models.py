from django.db import models

# Create your models here.
class student(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  email = models.TextField()
  address = models.TextField(null=True, blank=True)

class Car(models.Model):
  car_name = models.CharField(max_length=100)
  speed = models.IntegerField(default=50)



