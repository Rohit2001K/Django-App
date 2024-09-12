from django.urls import path
from . import views

urlpatterns=[
    path('',views.project_home,name='project_home'),
    path('<str:pk>/',views.detail_project,name='detail_project')
]