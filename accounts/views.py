from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# from django.http import HttpResponseRedirect,HttpResponse
# from a2 import urls
# from django.urls import reverse
# from django.template import loader



# Create your views here.
def home(request):
    # template = loader.get_template("index.html")
    # return HttpResponse(template.render())
    return render(request,"index.html")

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect("register/")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect("register/")
            else:
                user = User.objects.create_user(username=username,first_name = firstname,last_name=lastname,email=email,password=password1)
                user.save()
        else:
            messages.info(request,"Wrong password")
            return redirect("register")

        # for i in range(20):
        #     print("**************")
        # print("Info stored in a user database")
        # return HttpResponseRedirect(reverse('home'))
        return redirect('/')
    
    else:
        return render(request,"register.html")
    
    