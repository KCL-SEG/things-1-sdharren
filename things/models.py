from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(blank=True, max_length=120)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])