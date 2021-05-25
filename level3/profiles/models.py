from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class ProfileStatus(models.Model):
    userp = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "statuses"

    def __str__(self):
        return str(self.userp)