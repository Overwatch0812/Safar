from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from .models import Place,hotel,contactus
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from safar2 import settings
from django.db.models import Q


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

@login_required
def hotel_details(request, id):
    hotel2=hotel.objects.get(id=id)
    return render(request,'hotel_details.html',{'hotel':hotel2})

def chatbot(request):
    return render(request,'chatbot.html')

@login_required
def search(request):
    if request.method=='POST':
        search=request.POST['search']
        place=Place.objects.filter(Q(place_name__icontains=search)|Q(state_name__icontains=search) )
        return render(request,'search.html',{'place':place})
    else:
        return render(request,'search.html')