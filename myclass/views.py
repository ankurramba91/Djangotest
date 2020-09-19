from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import studentSerializer
from .models import studentData
import requests
# from .forms import RegisterForm

# Create your views here.

class studentViewset(viewsets.ModelViewSet):
    queryset  = studentData.objects.all()
    serializer_class = studentSerializer




def studentlist(request):
    response = requests.get("http://127.0.0.1:8000/home/myclass/").json()
    return render(request,'myclass/home.html',{'response':response})



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']

        x = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        x.save()
        return redirect ('/')
    else:
            
        return render(request, 'myclass/signup.html')