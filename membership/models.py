from django.db import models

from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):
    username = models.CharField(max_length = 100, unique=True)
    age = models.IntegerField()
    goal = models.TextField()
    address = models.TextField()
    


