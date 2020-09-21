from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import studentSerializer
from .models import studentData
import requests
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth


# Create your views here.

class studentViewset(viewsets.ModelViewSet):
    queryset  = studentData.objects.all()
    serializer_class = studentSerializer

@login_required
def studentlist(request):
    response = requests.get("http://127.0.0.1:8000/home/myclass/").json()
    return render(request,'myclass/index.html',{'response':response})

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, Your Profile is created. Please login below')
            return redirect('login')
    else:
        form = RegisterForm()
    return render (request,'myclass/signup.html', {'form':form})


def logout(request):
    auth.logout(request)
    return redirect('login')