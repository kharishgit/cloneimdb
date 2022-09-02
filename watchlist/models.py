from django.db import models

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
