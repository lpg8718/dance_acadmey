from django.db import models

class mstuser(models.Model):
    id=models.AutoField(primary_key=True)
    fnm=models.CharField(max_length=50)
    email=models.EmailField(max_length=80, unique=True)
    mno=models.CharField(max_length=10, unique=True)
    dob=models.CharField(max_length=15)
    pwd=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    address1=models.CharField(max_length=100)
    address2=models.CharField(max_length=100)
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    region=models.CharField(max_length=50)
    pin=models.IntegerField()
    role=models.CharField(max_length=50)
    image=models.FileField(upload_to='uploads/')

class contect(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mno=models.CharField(max_length=13)
    subject=models.CharField(max_length=100)
    msg=models.CharField(max_length=500)
