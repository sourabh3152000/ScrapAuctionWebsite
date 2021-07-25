from django.shortcuts import render,redirect
from django.conf import settings

from myadmin import models as myadmin_models
from . import models

import time

media_url=settings.MEDIA_URL

#middleware to check session for user routes
def sessioncheckusers_middleware(get_response):
    def middleware(request):
        if request.path=='/users/' or request.path=='/users/vdeals/' or request.path=='/users/vscdeals/' or request.path=='/users/vpdeals/' or request.path=='/users/bidproduct/':
            if request.session['sunm']==None or request.session['srole']!="user":
                response = redirect('/login/')
            else:
                response = get_response(request)
        else:
            response = get_response(request)
        return response
    return middleware

# Create your views here.
def userhome(request):
    
    
    return render(request,"userhome.html",{"sunm":request.session['sunm']})



def vdeals(request):
    clist=myadmin_models.Category.objects.all()
    return render(request,"vdeals.html",{"clist":clist,"media_url":media_url,"sunm":request.session['sunm']})

def vscdeals(request):
    catid=request.GET.get("catid")
    sclist=myadmin_models.SubCategory.objects.filter(catid=int(catid)) 
    return render(request,"vscdeals.html",{"sclist":sclist,"media_url":media_url,"sunm":request.session['sunm']})

def vpdeals(request):
    subcatid=request.GET.get("subcatid")
    plist=myadmin_models.Product.objects.filter(subcatid=int(subcatid)) 
    return render(request,"vpdeals.html",{"plist":plist,"media_url":media_url,"sunm":request.session['sunm']})


def bidproduct(request):
    if request.method=="GET":
        pid=request.GET.get("pid")
        pDetails=myadmin_models.Product.objects.filter(pid=int(pid))

        bDetails=models.Bidding.objects.filter(productid=int(pid))
        if len(bDetails)>0:
            cbprice=bDetails[0].bidprice
            for row in bDetails:
                if row.bidprice>cbprice:
                    cbprice=row.bidprice
        else:
            cbprice=pDetails[0].bprice



        if (time.time()-float(pDetails[0].info))>172800:
            bstatus=0

        else:
            bstatus=1
        return render(request,"bidproduct.html",{"bstatus": bstatus,"cbprice":cbprice,"pDetails":pDetails[0],"media_url":media_url,"sunm":request.session['sunm']})
    
    else:
        p=models.Bidding(productid=request.POST.get('pid'),uid=request.POST.get('uid'),bidprice=request.POST.get('bidprice'),info=time.asctime())
        p.save()
        return redirect("/users/bidproduct/?pid="+str(request.POST.get('pid')))



def bidresult(request):
    pid=request.GET.get("pid")
    bidlist=models.Bidding.objects.filter(productid=int(pid)) 
    return render(request,"bidresult.html",{"bidlist":bidlist,"media_url":media_url,"sunm":request.session['sunm']})




    







