from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
# Create your models here.
class UsersModel(AbstractUser, PermissionsMixin):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # field yang mana yang mau dihapus
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email