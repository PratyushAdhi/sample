from django.db import models
from django.contrib.auth import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ToDo(models.Model):
    text = models.CharField(max_length=120)
    priority = models.BooleanField(default=False)
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return f"{self.text} by {self.customer}"


class Customer(AbstractUser):
    username = models.CharField(max_length=120, unique=True)
    email = models.EmailField()
    priority = models.ForeignKey(
        ToDo, on_delete=models.CASCADE, null=True, related_name='customers')
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email
