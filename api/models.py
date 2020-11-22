from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50)

    def __str__(self, *args, **kwargs):
        return self.nickname
