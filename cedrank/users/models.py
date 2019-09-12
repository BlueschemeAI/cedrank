from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=20)
    company_id = models.CharField(max_length=10)
    phone = models.IntegerField()

    def __str__(self):
        return self.user.username

