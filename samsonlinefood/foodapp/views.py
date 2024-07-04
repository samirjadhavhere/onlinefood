from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render (request,"home.html")



# Create your views here.
from .models import *
def reguser(request):
    if request.method=="POST":
        name=request.POST.get("username")
        city=request.POST.get("usercity")
        email=request.POST.get("useremail")
        password=request.POST.get("password")
        obj=register()
        obj.username=name
        obj.city=city
        obj.email=email
        obj.password=password
        obj.save()
        return redirect("/")
    else:
        return render(request,"register1.html")
    
    

from django.contrib.auth import login,logout,authenticate
from django.contrib import messages as m
def userlogin(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pswd=request.POST.get("password")
        user=authenticate(request,username=uname,password=pswd)
        print(user)
        if user is not None:
            request.session["id"]=user.id
            login(request,user)
            m.success(request,"Login Successfull")
            return redirect("/")
        else:
            m.warning(request,"invalid username or password")
            d={"form":Loginform}
            return render(request,"login.html",d)
    else:
        d={"form":Loginform}
        return render(request,"login.html",d)