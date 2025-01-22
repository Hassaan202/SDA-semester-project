from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#Mujtaba
class Subject(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.name}"


class Discussion(models.Model):
    content = models.TextField()
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    subj_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.User_ID, self.subj_name}"


#Burhan
class ResourceUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')  # Default upload path
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[ {self.file.name} ] uploaded by {self.user.username}"



class ResourcesLib(models.Model):
    #this allows restricting the file types that can be uploaded
    FILE_TYPES = [
        ('books', 'books'),
        ('pastpapers', 'pastpapers'),
        ('playlists', 'playlists'),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    fileName = models.CharField(max_length=100)
    fileType = models.CharField(max_length=50, choices=FILE_TYPES)
    fileLink = models.URLField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fileName} - {self.subject.name} - {self.fileType}"