from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from myproject import models as myproject_models
from . import models

import time

#Middleware function to check user details at application level

def sessioncheckmyadmin_middleware(get_response):
    def middleware(request):
        if request.path=='/myadmin/' or request.path=='/myadmin/manageusers/' or request.path=='/myadmin/manageuserstatus/' or request.path=='/myadmin/managecategories/' or request.path=='/myadmin/managesubcategories/' or request.path=='/myadmin/manageproduct/':
            if request.session['sunm']==None or request.session['srole']!="admin":
                response = redirect('/login/')
            else:
                response = get_response(request)
        else:
            response = get_response(request)
        return response
    return middleware
        

# Create your views here.

def adminhome(request):
    return render(request,"adminhome.html",{"sunm":request.session["sunm"]})

def manageusers(request):
     userDetails=myproject_models.Register.objects.filter(role="user")
     return render(request,"manageusers.html",{"userDetails":userDetails,"sunm":request.session["sunm"]})

def manageuserstatus(request):
    s=request.GET.get("s")
    regid=request.GET.get("regid")
    if s=="block":
        myproject_models.Register.objects.filter(regid=regid).update(status=0)
    elif s=="verify":
         myproject_models.Register.objects.filter(regid=regid).update(status=1)
    else:
        myproject_models.Register.objects.filter(regid=regid).delete()
    return redirect('/myadmin/manageusers/')

def managecategories(request):
    if request.method=="GET":
        return render(request,"managecategories.html",{"output":"" ,"sunm":request.session["sunm"]})
    else:
        catnm=request.POST.get("catnm")
        caticon=request.FILES["caticon"]
        fs = FileSystemStorage()
        filename = fs.save(caticon.name,caticon)
        p=models.Category(catnm=catnm,caticonnm=filename)
        p.save()
        return render(request,"managecategories.html",{"output":"Category added Sucessfully..... ","sunm":request.session["sunm"]})
    

def managesubcategories(request):
    clist=models.Category.objects.all()
    if request.method=="GET":
        return render(request,"managesubcategories.html",{"output":"","clist":clist,"sunm":request.session["sunm"]})
    else:
        catid=request.POST.get("catid")
        subcatnm=request.POST.get("subcatnm")
        caticon=request.FILES["caticon"]
        fs = FileSystemStorage()
        filename = fs.save(caticon.name,caticon)
        p=models.SubCategory(catid=catid,subcatnm=subcatnm,subcaticonnm=filename)
        p.save()
        return render(request,"managesubcategories.html",{"output":"SubCategory added Sucessfully..... ","clist":clist,"sunm":request.session["sunm"]})


def manageproduct(request):
    clist=models.Category.objects.all()
    if request.method=="GET":
        return render(request,"manageproduct.html",{"clist":clist,"output":"","sunm":request.session["sunm"]})
    else:
        title=request.POST.get("title")
        catid=request.POST.get("catid")
        subcatid=request.POST.get("subcatid")
        pdescription=request.POST.get("pdescription")
        bprice=request.POST.get("bprice")
        info=time.time()


        picon=request.FILES["picon"]
        fs = FileSystemStorage()
        filename = fs.save(picon.name,picon)

        p=models.Product(title=title,catid=catid,subcatid=subcatid,pdescription=pdescription,bprice=bprice,piconnm=filename,info=info)
        p.save()

        return render(request,"manageproduct.html",{"clist":clist,"output":"Auction Product Added Sucessfully....","sunm":request.session["sunm"]})


def fetchSubCategory(request):
    catid=request.GET.get("catid")
    sclist=models.SubCategory.objects.filter(catid=int(catid))
    sclist_options="<option>Select Sub Category</option>"
    for row in sclist:
        sclist_options+=("<option value='"+str(row.subcatid)+"'>"+row.subcatnm+" </option>")
    return HttpResponse(sclist_options)


def viewproduct(request):
    plist=models.Product.objects.all()

    return render(request,"viewproduct.html",{"sunm":request.session["sunm"],"plist":plist})




    
