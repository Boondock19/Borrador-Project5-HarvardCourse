from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.
def index(request):
    Medics=Medic.objects.all()
    context={"Medics":Medics}
    return render(request,"MedicPlace/index.html",context)

def login_view(request):
    if request.method=="POST":
        username=request.POST["Username"]
        password=request.POST["Password"]
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"MedicPlace/login.html",{"message":"Invalid username and/or password"})
    else:
        return render(request,"MedicPlace/login.html")        

def register_view(request):
    if request.method=="POST":
        username=request.POST["Username"]
        email=request.POST["Email"]
        password=request.POST["Password"]
        confirmation=request.POST["Confirmation"]
        First_Name=request.POST["First_name"]
        Last_Name=request.POST["Last_name"]
        age=request.POST["age"]
        is_dr=request.POST["is_dr"]
        if int(age)<18:
            return render(request,"MedicPlace/register.html",{"message":"Age must be 18 or more"}) 
        if  First_Name=="":
             return render(request,"MedicPlace/register.html",{"message":"Please fill all the fields"})
        if  Last_Name=="":
             return render(request,"MedicPlace/register.html",{"message":"Please fill all the fields"})
        if password != confirmation:
            return render(request,"MedicPlace/register.html",{"message":"Passwords must be the same"})

        try:
            NewUser=User.objects.create_user(username,email,password)
            
        except IntegrityError:
            return render(request,"MedicPlace/register.html",{"message":"Username already exist"})
        
        if is_dr=="Yes":
            if  request.POST["Clinic"]=="":
             return render(request,"MedicPlace/register.html",{"message":"Please fill the clinic field"})
            NewDr=Medic()
            NewDr.user=NewUser
            NewDr.First_Name=First_Name
            NewDr.Last_Name=Last_Name
            NewDr.Clinic=request.POST["Clinic"]
            NewDr.age=age
            NewDr.rate=0.0
            NewDr.save()
            NewUser.save()
        elif is_dr=="No":
            NewNormalUser=Normal_User()
            NewNormalUser.user=NewUser
            NewNormalUser.First_Name=First_Name
            NewNormalUser.Last_Name=Last_Name
            NewNormalUser.age=age
            NewNormalUser.save()
            NewUser.save()
        else:
            return render(request,"MedicPlace/register.html",{"message":"You must say if your a Dr or not"})
        
        login(request,NewUser)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"MedicPlace/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def data_sheet(request,id):
    Medics=Medic.objects.filter(user__id=id)
    Normal_Users=Normal_User.objects.filter(user__id=id)
    if len(Medics)>0:
      data_sheet_user=Medics[0]
      message="Entro en la parte de medic"
      Page_type="Medic"
    elif len(Normal_Users)>0:
        data_sheet_user=Normal_Users[0]
        message="Entro en la parte de Normal User"
        Page_type="Normal_User"
    context={"data_sheet_user":data_sheet_user,"message":message,"Page_type":Page_type}
    return render(request,"MedicPlace/data_sheet.html",context)