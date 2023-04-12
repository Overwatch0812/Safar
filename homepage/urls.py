from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('AboutUs',views.AboutUs,name='AboutUs'),
    path('Blogs',views.Blogs,name='Blogs'),
    path('contactuss',views.contactuss,name='contactuss'),
    path('hotels/<str:place_name>',views.hotels,name='hotels'),
    path('place_details/<int:id>',views.place_details,name='place_details'),
    path('hotel_details/<int:id>',views.hotel_details,name='hotel_details'),
    path('chatbot',views.chatbot,name='chatbot'),
]