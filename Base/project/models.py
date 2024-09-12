from django.db import models
from users.models import Profile
import uuid
# Create your models here.

class Project(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    title=models.CharField(max_length=50)
    discription=models.TextField(max_length=500)
    created=models.DateTimeField(auto_now_add=True)
    reviews=models.IntegerField(default=0,blank=True,null=True)
    reviews_ratio=models.IntegerField(default=0,blank=True,null=True)
    project_img=models.ImageField(default='/pro/pro.jpg')
    def __str__(self):
        return str(self.title+' Projects')

    class Meta:
        db_table='projects'
        ordering=['-created']



class Review(models.Model):
    VOTE_TYPE=(
        ('Up','Like'),
        ('Down','Dislike')
    )
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    body=models.TextField(blank=True,null=True)
    value=models.CharField(max_length=200,choices=VOTE_TYPE)

    class Meta:
        unique_together=[['owner','project']]

    def __str__(self):
        return str(self.value)