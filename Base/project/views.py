from django.shortcuts import render,redirect
from . models import Project,Review
from.forms import review_form
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.


def project_home(request):
    data=Project.objects.all()
    content={
        'data':data
    }
    return render(request,'project/home.html',content)


#Projects detail page

def detail_project(request,pk):
    detail=Project.objects.filter(id=pk)
    detail1=Project.objects.get(id=pk)
    form=review_form()

    try:
        if request.method=='POST':
            form=review_form(request.POST)
            rev=form.save(commit=False)
            rev.project=detail1
            rev.owner=request.user.profile
            rev.save()
            messages.success(request,'Your review is added')

    except:
        messages.error(request,"You cannot submit more than 1 review for 1 game")

    context={
        'detail':detail,
        'form': form,
        
    }
    return render(request,'project/subpro.html',context)

def delete_review(request,pk):
    review = Review.objects.get(id=pk)
    
    