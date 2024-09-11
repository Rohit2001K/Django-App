from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,null=False)
    email=models.EmailField(unique=True)
    bio=models.TextField(max_length=500)
    id=models.UUIDField(default=uuid.uuid1,primary_key=True)
    pic=models.ImageField(default='user.jpg')
    
    def __str__(self):
        return str(self.name)
