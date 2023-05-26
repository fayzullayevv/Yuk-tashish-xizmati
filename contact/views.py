from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *


@login_required(login_url='login')
def indexview(request):
    return render(request,'index.html')



def SignUp(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2 or len(password1)<8:
            messages.error(request,'Your password must be the same and contain more than 8 characters!')
            return redirect('signup')
        my_users = User.objects.create_user(username=username,password=password1)
        my_users.save()
        return redirect('login')
    return render(request,'registration/signup.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['login_username']
        password = request.POST['login_password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user) 
            username = user.username
            return render(request,'index.html',{'username':username})

        else:
            messages.error(request,'You entered your login or password incorrectly, please try again!')
            return redirect('login')
      
    return render(request,'registration/login.html')


def LogOut(request):
    logout(request)
    return redirect('signup')


@login_required(login_url='login')
def ChooseView(request):
    context = ChooseModel.objects.all()
    return render(request,'choose.html',{'context':context})



def InfoView(request,name):
    obj = InfoModel.objects.get(mashina=name)
    if request.method == 'POST':
        mashina = obj.mashina
        manzildan = request.POST.get('Location')
        manzilga = request.POST.get('To destination')
        email1 = request.POST.get('Email')
        raqam1 = request.POST.get('Contact Number')        
        buyrutma = BuyurtmaBerishModel.objects.create(mashina=mashina,manzildan=manzildan,manzilga=manzilga,email1=email1,raqam1=raqam1)
        buyrutma.save()
        return redirect('choose')
    return render(request,'info.html',{'obj':obj})
