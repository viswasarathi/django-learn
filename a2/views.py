from django.shortcuts import render
from .models import Places

# Create your views here.

def index(request):
    place1 = Places()
    place1.name = "chennai"
    return render(request,"index.html",{"place1":place1})

