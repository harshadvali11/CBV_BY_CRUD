from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from app.models import *
class SchoolList(ListView):
    model=School
    #queryset=School.objects.all()
    context_object_name='schools'
    #template_name='app/school_list.html'
    #ordering=['scname']