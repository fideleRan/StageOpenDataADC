from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.contributeur.models import Contributeur


# Create your models here.

class User(AbstractUser):
    is_adminUser = models.BooleanField(default=False)
    is_contributeur = models.BooleanField(default=True)
    contributeur = models.ForeignKey(Contributeur, on_delete=models.CASCADE, null=True)