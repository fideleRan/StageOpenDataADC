from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_adminUser = models.BooleanField(default=False)
    is_contributeur = models.BooleanField(default=True)