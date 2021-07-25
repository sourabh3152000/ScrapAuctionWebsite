#Templates Pages

from django.http import HttpResponse
from django.shortcuts import render,redirect
import time
from . import models

#middleware to check session for mainapp routes
def sessioncheck_middleware(get_response):
     def middleware(request):
          if request.path=='' or request.path=='/home/' or request.path=='/about/' or  request.path=='/contact/' or  request.path=='/service/' or  request.path=='/register/' or  request.path=='/login/':
               request.session['sunm']=None
               request.session['srole']=None

               response= get_response(request)

          else:
               response=get_response(request)
          return response
     return middleware




def home(request):
     return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
     return render(request,"contact.html")

def service(request):
     return render(request,"service.html")

def register(request):
     if request.method=="GET":
          return render(request,"register.html",{"output":""})
     else:
          name=request.POST.get("name")
          username=request.POST.get("username")
          password=request.POST.get("password")
          mobile=request.POST.get("mobile")
          address=request.POST.get("address")
          city=request.POST.get("city")
          gender=request.POST.get("gender")
          info=time.asctime()
          p=models.Register(name=name,username=username,password=password,mobile=mobile,address=address,city=city,gender=gender,role="user",status=0,info=info)
          p.save()

          return render(request,"register.html",{"output":"User register successfully....."})

def checkEmail(request):
     emailid=request.GET.get("emailid")
     result=models.Register.objects.filter(username__startswith=emailid).exists()
     if result:
          s=1
     else:
          s=0
     
     return HttpResponse(s)


def login(request):
     if request.method=="GET":
          return render(request,"login.html",{"output":""})
     else:
          username=request.POST.get("username")
          password=request.POST.get("password")
          userDetails=models.Register.objects.filter(username=username,password=password,status=1)
          if len(userDetails)>0:
               #to store user details in session
               request.session['sunm']=userDetails[0].username
               request.session['srole']=userDetails[0].role

               if userDetails[0].role=="admin":
                    return redirect('/myadmin/')
               else:
                    return redirect('/users/')

          else:
                return render(request,"login.html",{"output": "Invailid User/ Verify Your Account"})

          
