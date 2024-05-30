from django.db import models
from django.contrib.auth.models import User

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    receive_newsletters = models.BooleanField(default=True)
    public_profile = models.BooleanField(default=True)

    def __str__(self):
        return f'Settings for {self.user.username}'