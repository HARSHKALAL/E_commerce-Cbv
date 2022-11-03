from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    logo=models.ImageField(upload_to="user/logo/",blank=True,null=True)
