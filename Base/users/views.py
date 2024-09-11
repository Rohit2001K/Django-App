from django.shortcuts import render
from .models import Profile
# Create your views here.


#home page view
def home(request):
    data=Profile.objects.all()
    content={
        'data':data
    }
    return render(request,'users/home.html',content)