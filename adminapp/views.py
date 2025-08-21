from django.shortcuts import redirect, render, redirect
from django.http import HttpResponse

from my1.models import mstuser

from . import models
from django.contrib.auth import logout


def sessioncheckadmin_middleware(get_response):
 def middleware(request):
    if request.path=='/adminhome/' or request.path=='/adminhome/contect/'  or request.path=='/adminhome/image_show/' or request.path=='/adminhome/admin_update_profile/' or request.path=='/adminhome/addstudent/' or request.path=='/adminhome/student_update/' or request.path=='/adminhome/studentlist/' or request.path=='/adminhome/addbatch/' or request.path=='/adminhome/course_update/' or request.path=='/adminhome/course_update_record/' or request.path=='/adminhome/course_delete/' or request.path=='/adminhome/courselist/' or request.path=='/adminhome/batch_update/' or request.path=='/adminhome/batch_update_record/' or request.path=='/adminhome/batch_delete/' or request.path=='/adminhome/batchlist/': 
      if "email" not in request.session:  
            response=redirect('/login/')
      else:
            response=get_response(request)
    else:
        response=get_response(request)
    return response
 return middleware 


# Create your views here.
# admin home page=====================================================
def adminhome(request):
    # for fetching data from session-----===
    name=request.session.get('fnm')
    role=request.session.get('role')
    email=request.session.get('email')
    image1=request.session.get('image')
    # ------------------------------------------
    image=mstuser.objects.filter(email=email)
    print("name:",name)
    print("role: ",role)
    print("email:",email)
    print("image_path",image1)
    # print(image1)
    return render(request,'adminhome.html',{'name':name,'role':role,'img':image1 } )
# ======================================================================

# =========add course====================================================
def addcourse(request):
    if request.method=='GET':
       image1=request.session.get('image')
       return render(request,'addcourse.html',{'img':image1})
    else:
        # ////////////
        image1=request.session.get('image')
        # //////////
        category=request.POST.get('category')
        coursename=request.POST.get('coursename')
        duration=request.POST.get('duration')
        fees=request.POST.get('fees')
        coursedetail=request.POST.get('coursedetail')
        print(category,coursename,duration,fees,coursedetail)
        res=models.course(category=category,coursename=coursename,duration=duration,fees=fees,coursedetail=coursedetail)
        res.save()
        print('Data Saved Successfully......')
        return render(request,'addcourse.html' , {'msg1':'Data Saved Successfully !!','img':image1})
    
# ------------=================================================================
# ---------Add student=----------------------------------------------------------

def addstudent(request):
    if request.method=="GET":
        image1=request.session.get('image')
        return render(request,'addstudent.html',{'img':image1})
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

        image1=request.session.get('image')


        print(fnm,email,mno,dob,pwd,gender,address1,address2,country,city,region,pin)
        if mstuser.objects.filter(email=email):
            return render(request,'addstudent.html',{'msg2':'Email Already Exists..',"img":image1})
        elif mstuser.objects.filter(mno=mno):
            return render(request,'addstudent.html',{'msg2':'Mobile number Already Exists..','img':image1})
        else:
            res=mstuser(fnm=fnm,email=email,mno=mno,dob=dob,pwd=pwd,gender=gender,address1=address1,address2=address2,country=country,city=city,region=region,pin=pin, role=role, image=image)
            res.save()
            return render(request,'addstudent.html',{'msg1':'Data Saved Successfully','img':image1})
        


        
    
# ========Print course========================================================

def courselist(request):
    res=models.course.objects.all()
    image1=request.session.get('image')
    return render(request, 'courselist.html',{'res':res,'img':image1})
# ==============================================================================

# ========Add Batch========================================================

def addbatch(request):
    image1=request.session.get('image')
    if request.method=='GET':
        res=models.course.objects.all()
        return render(request,'addbatch.html' , {'res':res,'img':image1})
    else:
        courseid=request.POST.get('courseid')
        batchtitle=request.POST.get('batchtitle')
        startdate=request.POST.get('startdate')
        instname=request.POST.get('instname')
        batchtime=request.POST.get('batchtime')

        res=models.batch(courseid_id=courseid,batchtitle=batchtitle,startdate=startdate,instname=instname,batchtime=batchtime)
        res.save()
        print('Data Saved Successfully......')
        res=models.course.objects.all()
        return render(request,'addbatch.html' , {'img':image1,'msg2':'Data Saved Successfully !!' , 'res':''})
# ================================================================================================

# ===Batch list=============================================================================
def batchlist(request):
    image1=request.session.get('image')
    res=models.batch.objects.filter(batchstatus=1)
    return render(request, 'batchlist.html',{'res':res,'img':image1})



# ===========Batch Update ============================================================================

def batch_update(request):
       res=models.batch.objects.all()
       image1=request.session.get('image')
       return render(request, 'batch_update.html',{'res':res ,'img':image1})


def batch_update_record(request):
    image1=request.session.get('image')
    if request.method=="GET":
        batchid=request.GET.get("batchid")
        res1=models.course.objects.all()
        res=models.batch.objects.filter(batchid=batchid)
        return render(request,"batch_update_record.html",{'res':res,'res1':res1,'img':image1})
    else:
        batchid=request.POST.get('batchid')
        courseid=request.POST.get('courseid')
        batchtitle=request.POST.get('batchtitle')
        startdate=request.POST.get('startdate')
        instname=request.POST.get('instname')
        models.batch.objects.filter(batchid=batchid).update(courseid_id=courseid,batchtitle=batchtitle,startdate=startdate,instname=instname)
        return redirect("/adminhome/batchlist/")
# ===============================================================================================


# =====course Update=================================================================
def course_update(request):
     res=models.course.objects.all()
     image1=request.session.get('image')
     return render(request, 'course_update.html',{'res':res,'img':image1})

# ====================================================================================


# ====update record==================================================================
def course_update_record(request):
    image1=request.session.get('image')
    if request.method=="GET":
      courseid=request.GET.get("courseid")
      res=models.course.objects.filter(courseid=courseid)
      return render(request,"course_update_record.html",{'res':res,'img':image1})
    else:
        category=request.POST.get("category")
        coursename=request.POST.get("coursename")
        duration=request.POST.get("duration")
        fees=request.POST.get("fees")
        coursedetail=request.POST.get("coursedetail")
        courseid=request.POST.get("courseid")

        print(category,coursename,duration,fees,coursedetail)
        models.course.objects.filter(courseid=courseid).update(category=category,coursename=coursename,duration=duration,fees=fees,coursedetail=coursedetail)
        print(" Update .. !")
        return redirect("/adminhome/courselist/")
# ==================================================================================

# ---------student update--------------------------------------------------------

def student_update(request):
    image1=request.session.get('image')
    res=mstuser.objects.filter(role='student')
    return render(request,'student_update.html',{'res':res,'img':image1})

def student_update_record(request):
    image1=request.session.get('image')
    if request.method=='GET':
       id=request.GET.get("id")
       res=mstuser.objects.filter(id=id)
       return render(request, 'student_update_record.html',{'result':res,'img':image1})
    else:
        fnm=request.POST['fnm']
        id=request.POST['id']
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
        return redirect("/adminhome/studentlist/")
# ========profile update============================================

def admin_update_profile(request):
    image1=request.session.get('image')
    if request.method=='GET':
        email=request.session.get("email")
        res=mstuser.objects.filter(email=email)
        return render(request,"admin_update_profile.html",{ 'res':res ,'img':image1})
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
        return redirect('/adminhome/')
           

# =======delete=====================================================

def student_delete(request):
    res=mstuser.objects.filter(role='student')
    image1=request.session.get('image')
    return render(request,'student_delete.html',{'res':res, 'img':image1})

def delstudent(request):
    id=request.GET.get('id')
    res=mstuser.objects.get(id=id)
    res.delete()
    return redirect("/adminhome/student_delete/")




def course_delete(request):
    res=models.course.objects.all()
    image1=request.session.get('image')
    return render(request, 'course_delete.html',{'res':res,'img':image1})

def delcourse(request):
    
    courseid=request.GET.get('courseid')
    res=models.course.objects.get(courseid=courseid)
    res.delete()
    return redirect("/adminhome/course_delete/")




def batch_delete(request):
    image1=request.session.get('image')

    res=models.batch.objects.all()
    return render(request, 'batch_delete.html',{'res':res,'img':image1})

def delbatch(request):
    batchid=request.GET.get('batchid')
    res=models.batch.objects.get(batchid=batchid)
    res.delete()
    return redirect("/adminhome/batch_delete/")




def studentlist(request):
    image1=request.session.get('image')

    res=mstuser.objects.filter(role='student')
    return render(request,"studentlist.html",{"res":res, 'img':image1})



def image_upload(request):
    image1=request.session.get('image')

    if request.method=='POST':
       image=request.FILES['image']
       name=request.POST.get('name')
       print(image,name)
       res=models.eventimage(name=name, image=image)
       res.save()
       return render(request,"image_upload.html",{'msg1':'save','img':image1})
    else:
        return render(request,"image_upload.html",{'msg1':'','img':image1})


def image_show(request):
    image1=request.session.get('image')

    res=models.eventimage.objects.all()
    print(res)
    return render(request,"image_show.html",{'res':res,'img':image1})


def contect(request):
    image1=request.session.get('image')

    return render(request,"admincontect.html",{'img':image1})


def logout1(request):
  logout(request)
  return redirect('http://localhost:8000/')
