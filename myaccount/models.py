from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(AbstractUser):
    ROLE_CHOICES = (
        ('instructor', 'Instructor'),
        ('user', 'User')
    )
    email = models.EmailField(default='example@example.com')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
