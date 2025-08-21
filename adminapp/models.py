from django import forms
from django.db import models

# Create your models here.
class course(models.Model):
    courseid=models.AutoField(primary_key=True)
    category=models.CharField(max_length=34)
    coursename=models.CharField(max_length=34)
    duration=models.CharField(max_length=34)
    fees=models.IntegerField()
    coursedetail=models.CharField(max_length=100)

class batch(models.Model):
    courseid=models.ForeignKey('course',on_delete=models.CASCADE)
    batchid=models.AutoField(primary_key=True)
    batchtitle=models.CharField(max_length=50)
    startdate=models.CharField(max_length=20)
    batchtime=models.CharField(max_length=10)
    instname=models.CharField(max_length=40)
    batchstatus=models.IntegerField(default=1)


class eventimage(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    image=models.FileField(upload_to='uploads/')