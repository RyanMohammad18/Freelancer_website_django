from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass

    def get_freelancer(self):
        if(hasattr(self,'freelancer')):
            return self.freelancer    
        return None
    
    def get_business(self):
        if(hasattr(self,'business')):
            return self.business    
        return None