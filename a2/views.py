from django.shortcuts import render
from .models import Places

# Create your views here.

def index(request):
    place1 = Places()
    place1.name = "chennai"
    place1.cap = "hot city"
    place1.review = 4
    place1.offer = False

    
    place2 = Places()
    place2.name = "coimbatore"
    place2.cap = "chill city - manchester of tamilnadu"
    place2.review = 5
    place2.offer = True

    place3 = Places()
    place3.name = "madurai"
    place3.cap = "moderate city"
    place3.review = 4
    place3.offer = False

    allPlace = [place1,place2,place3]

    return render(request,"index.html",{"places":allPlace})

