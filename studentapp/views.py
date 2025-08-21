from django.shortcuts import redirect, render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from my1.models import mstuser
from adminapp.models import course , batch, eventimage
from . import models
import datetime
# Create your views here.

def sessioncheckuser_middleware(get_response):
 def middleware(request):
    if request.path=='/studenthome/'  or request.path=='/studenthome/gallery1/' or request.path=='/studenthome/student_course_list/' or request.path=='/studenthome/student_batch_list/' or request.path=='/studenthome/updateprofile/' or request.path=="/studenthome/enroll_batch/" or request.path=="/studenthome/profile/": 
      if "email" not in request.session:  
            response=redirect('/login/')
      else:
            response=get_response(request)
    else:
        response=get_response(request)
    return response
 return middleware 


# admin home page=====================================================
def studenthome(request):
    # for fetching data from session-----===
    name=request.session.get('fnm')
    role=request.session.get('role')
    email=request.session.get('email')
    # ------------------------------------------
    image=request.session.get('image')
    print(name)
    print(role)
    print(email)
    print('image')

    return render(request,'studenthome.html',{'name':name,'role':role,'email':email,'image':image})


def updateprofile(request):
    image=request.session.get('image')
    if request.method=='GET':
        email=request.session.get("email")
        res=mstuser.objects.filter(email=email)
        return render(request,"updateprofile.html",{ 'res':res ,"image":image })
    else:
        id=request.POST['id']
        fnm=request.POST['fnm']
        email=request.POST['email']
        mno=request.POST['mno']
        dob=request.POST['dob']
        pwd=request.POST['pwd']
        gender=request.POST['gender']
        address1=request.POST['address1']
        address2=request.POST['address2']
        country=request.POST['country']
        city=request.POST['city']
        region=request.POST['region']
        pin=request.POST['pin']
        mstuser.objects.filter(id=id).update(fnm=fnm,mno=mno,dob=dob,pwd=pwd,gender=gender,address1=address1,address2=address2,country=country,city=city,region=region,pin=pin)
        return redirect('/studenthome/')


def student_course_list(request):
    res=course.objects.all()
    image=request.session.get('image')
    return render(request, 'student_course_list.html',{'res':res, 'image':image})

def student_batch_list(request):
    res=batch.objects.all()
    image=request.session.get('image')
    return render(request, 'student_batch_list.html',{'res':res , 'image':image})

def select_batch(request):
    image=request.session.get('image')
    if request.method=='GET':
        batchid=request.GET.get('batchid')
        res=batch.objects.filter(batchid=batchid)
        print(res)
        return render(request, 'select_batch.html',{'res':res, 'image':image})
    else:
        studentname=request.session.get('fnm')
        batchid=request.POST.get('batchid')
        batchtitle=request.POST.get('batchtitle')
        batchtime=request.POST.get('batchtime')
        startdate=request.POST.get('startdate')
        instname=request.POST.get('instname')
        email=request.session.get('email')
        print(email)
        print(batchid,batchtime,batchtitle,startdate,instname)
        res=models.selectbatch(studentname=studentname,email=email,batchid=batchid,batchtitle=batchtitle,startdate=startdate,batchtime=batchtime,instname=instname)
        res.save()
        print("save sucsessfully.....")
        return redirect('/studenthome/student_batch_list/')




def enroll_batch(request):
    image=request.session.get('image')
    email=request.session.get('email')
    print("Email :",email)
    res=models.selectbatch.objects.filter(email=email)
    return render(request,'enroll_batch.html',{'res':res, 'image':image})

def profile(request):
    image=request.session.get('image')
    email=request.session.get('email')
    res=mstuser.objects.filter(email=email)
    return render(request,'profile.html',{'res':res, 'image':image})

def gallery1(request):
       image=request.session.get('image')
       res=eventimage.objects.all()
       print(res)
       return render(request, 'gallery1.html' , {'res':res, 'image':image}) 

def logout1(request):
  logout(request)
  return redirect('http://localhost:8000/')


