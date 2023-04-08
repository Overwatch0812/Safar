from django.shortcuts import render
from django.contrib.auth.models import auth
from .models import Place
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    places=Place.objects.all()
    return render(request,'index.html',{'places':places})

def AboutUs(request):
    return render(request,'About.html')

def Blogs(request):
    return render(request,'blog.html')


@login_required
def place_details(request, id):
    place=Place.objects.get(id=id)
    return render(request,'place_details.html',{'place':place})