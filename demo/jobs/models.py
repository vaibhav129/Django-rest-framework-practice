from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class joboffer(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    title=models.CharField(max_length=150)
    salary=models.PositiveIntegerField()
    create=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
