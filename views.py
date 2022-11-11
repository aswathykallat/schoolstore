from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
from urllib import request


# Create your views here.

def index(request):
    return render (request,'index.html')

def registeration(request):
    if request.method=="POST":
        username=request.POST.get('username')
        
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        

        student(username=username,password=password,password2=password2).save()
        return redirect('login')
    else:
        return render(request,'registeration.html')  



def log(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        # print('email')
        # print(email)
        # print('password',password)
        # print('password')
        # print(password)

        cr=student.objects.filter(username=username,password=password)
        if cr:
            user=student.objects.get(username=username,password=password)
           
            cr==user

            return redirect('dash')
        else:
            return render(request,'login.html')
    else:
        return render(request,'registeration.html')


def login(request):
    return render (request,'login.html')

def dash(request):
    return render (request,'dash.html')




def dashboard(request):
   
    return render (request,'dashboard.html')

def dashview(request):
    return render (request,'dashview.html')
