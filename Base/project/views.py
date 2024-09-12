from django.shortcuts import render
from . models import Project
from.forms import review_form
from django.shortcuts import get_object_or_404, render
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

    
    if request.method=='POST':
        form=review_form(request.POST)
        rev=form.save(commit=False)
        rev.project=detail1
        rev.owner=request.user.profile
        rev.save()


    context={
        'detail':detail,
        'form': form,
    }
    return render(request,'project/subpro.html',context)