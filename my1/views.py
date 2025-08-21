from django.http import HttpResponse
from django.shortcuts import render, redirect

from my1 import models
from adminapp.models import course, batch, eventimage

from django.core.files.storage import FileSystemStorage

# from  email api
from . import emailAPI

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:
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
        image=request.FILES['image']
        role='student'
        print("image====",image)
        print(fnm,email,mno,dob,pwd,gender,address1,address2,country,city,region,pin,image)
        if models.mstuser.objects.filter(email=email):
            return render(request,'register.html',{'msg2':'Email Already Exists..'})
        elif models.mstuser.objects.filter(mno=mno):
            return render(request,'register.html',{'msg2':'Mobile number Already Exists..'})
        else:
            res=models.mstuser(fnm=fnm,email=email,mno=mno,dob=dob,pwd=pwd,gender=gender,address1=address1,address2=address2,country=country,city=city,region=region,pin=pin, role=role , image=image)
            res.save()
            # ----------------------------------------------------
            # to send varification
            emailAPI.sendMail(email,pwd)
            return render(request,'register.html',{'msg1':'Data Saved Successfully'})
     

def emailtesting(request):
    from . import emailAPItesting

    email="batchphp390@gmail.com"
    password="ekta123*"

    res=emailAPItesting.sendMail(email,password)
    return HttpResponse(res)



def login(request):
    if request.method=='GET':
        if request.COOKIES.get('email') is not None:
            email=request.COOKIES['email']
            pwd=request.COOKIES['pwd'] 
            return render(request,'login.html',{'email':email,'pwd':pwd})
        else:      
            return render(request,'login.html',{'email':''})
    else:
        email=request.POST['email']
        pwd=request.POST['pwd']
        remember=request.POST.get('remember')

        res=models.mstuser.objects.filter(email=email,pwd=pwd)
        if len(res)>0:

            role=res[0].role
            fnm=res[0].fnm
            image=res[0].image
            fs=FileSystemStorage()
            image_path=fs.url(image)
            print(role)
            print(fnm)
            print(image)
            print(image_path)
            # session creation======================
            request.session['role']=role
            request.session['email']=email
            request.session['fnm']=fnm
            request.session['image']=image_path
            
            # request.session.set_expiry(10)  # Session expires in 5 minutes (300 seconds)
            # ====COOKIES========================
            # if remember is not None:
            if(remember=='on'):
                if role=='admin':
                    response=redirect('/adminhome/')
                else:
                    response=redirect('/studenthome/')
                response.set_cookie("email",email)
                response.set_cookie("name",fnm)
                response.set_cookie("role",role)
                response.set_cookie("pwd",pwd)
                return response
            # ======================================            
            #=======================================
            if res[0].role=='admin':
                print('Welcome Admin')
                return redirect('/adminhome/')
            else:
                return redirect('/studenthome/')
        else:
            return render(request,'login.html',{'msg2':'Invalid User'})
        
def contect(request):
    if request.method=='GET':
        return render(request,"contect.html")
    else:
         name=request.POST.get('name')
         mno=request.POST.get('mno')
         email=request.POST.get('email')
         subject=request.POST.get('subject')
         msg=request.POST.get('msg')
         print("name=",name ,"email=",email)
         res=models.contect(name=name, mno=mno, email=email,subject=subject, msg=msg)
         res.save()
         print("save sucsessfully..")
         return render(request,"contect.html")

def courselist1(request):
    res=course.objects.all()
    return render(request, 'courselist1.html',{'res':res})

def batchlist1(request):
    res=batch.objects.filter(batchstatus=1)
    res2=course.objects.all()
    return render(request, 'batchlist1.html',{'res':res, 'res2':res2})

def gallery(request):
       res=eventimage.objects.all()
       print(res)
       return render(request, 'gallery.html' , {'res':res}) 

