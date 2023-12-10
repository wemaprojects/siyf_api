from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Manager(AbstractUser):
    locked = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"
        