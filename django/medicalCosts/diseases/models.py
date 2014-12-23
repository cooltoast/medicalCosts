from django.db import models
from django.utils import timezone

# Create your models here.
class Operation(models.Model):
  procedure = models.ForeignKey('Procedure')
  location = models.CharField(max_length=100)
  cost = models.PositiveIntegerField(default=0)
  date = models.DateTimeField(default=timezone.now(), blank=True)

class Procedure(models.Model):
  name = models.CharField(max_length=100)
  disease = models.ForeignKey('Disease')

  def __str__(self):
    return self.name

class Disease(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

