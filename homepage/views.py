from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from .models import Place,hotel,contactus
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    places=Place.objects.all()
    return render(request,'index.html',{'places':places})

def AboutUs(request):
    return render(request,'About.html')

def Blogs(request):
    return render(request,'blog.html')

def contactuss(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        message=request.POST['message']
        text=contactus.objects.get(id=request.user.id)
        text.name=name
        text.email=email
        text.message=message
        text.save()
        return redirect('/')
    else:
        return render(request,'contactus.html')

def hotels(request,place_name):
    hotels=hotel.objects.filter(location=place_name)
    return render(request,'hotel.html',{'hotels':hotels})


@login_required
def place_details(request, id):
    place=Place.objects.get(id=id)
    return render(request,'place_details.html',{'place':place})