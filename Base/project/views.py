from django.shortcuts import render
from . models import Project
# Create your views here.


def project_home(request):
    data=Project.objects.all()
    content={
        'data':data
    }
    return render(request,'project/home.html',content)