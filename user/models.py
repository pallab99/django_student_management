from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
