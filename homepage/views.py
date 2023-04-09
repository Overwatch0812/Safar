from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from .models import Place,hotel,contactus
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from safar2 import settings


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
        subject=request.POST['subject']
        message=request.POST['message']
        contact=contactus()
        contact.username=username
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()
        send_mail(subject,message,'backendlord08@gmail.com',[email])
        return redirect('/')
    else:
        user=User.objects.get(id=request.user.id)
        return render(request,'contactus.html',{'user':user})

def hotels(request,place_name):
    hotels=hotel.objects.filter(location=place_name)
    return render(request,'hotel.html',{'hotels':hotels})


@login_required
def place_details(request, id):
    place=Place.objects.get(id=id)
    return render(request,'place_details.html',{'place':place})