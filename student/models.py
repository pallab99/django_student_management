from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator


class Student(models.Model):
    name = models.CharField(unique=True, max_length=100,
                            validators=[MinLengthValidator(5)])
    age = models.IntegerField(validators=[MinValueValidator(
        18), MaxValueValidator(100)])
    address = models.CharField(max_length=100)
    student_id = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, default='9876543210')

    def __str__(self):
        return str(self.name)
