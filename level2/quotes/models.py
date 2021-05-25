from django.db import models

class quote(models.Model):
    author = models.CharField(max_length=150)
    body = models.TextField()
    context = models.CharField(max_length=200, blank=True)
    source = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author