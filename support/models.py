from django.db import models

# Create your models here.
class contactMessage(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    message=models.TextField()

    def __str__(self):
        return f"{self.name}, {self.email}, {self.subject}"