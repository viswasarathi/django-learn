from django.shortcuts import render
from .models import Places

# Create your views here.

def index(request):
    allPlace = Places.objects.all()

    return render(request,"index.html",{"places":allPlace})

