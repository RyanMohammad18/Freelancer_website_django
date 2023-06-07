from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



# Create your models here.
class Freelancer(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    tagline= models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    website= models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to ="profiles/", blank=True)

    def __str__(self):
        return f"{self.id} | {self.name}"
    
class Business(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    
    profile_pic = models.ImageField(upload_to ="profiles/", blank=True)


    def __str__(self):
        return f"{self.id} | {self.name}"