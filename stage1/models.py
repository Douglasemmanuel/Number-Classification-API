from django.db import models

# Create your models here.
class NumberProperties(models.Model):
    number = models.IntegerField()
    is_perfect = models.BooleanField()
    is_prime = models.BooleanField()
    properties = models.CharField(max_length=255)
    digital_sum = models.IntegerField()
    fun_fact = models.CharField(max_length=255)