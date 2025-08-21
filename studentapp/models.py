from django.db import models

# Create your models here.
class selectbatch(models.Model):
    sno=models.AutoField(primary_key=True)
    studentname=models.CharField(max_length=50)
    email=models.CharField(max_length=80)
    batchid=models.BigIntegerField()
    batchtitle=models.CharField(max_length=50)
    startdate=models.DateField()
    batchtime=models.CharField(max_length=20)
    instname=models.CharField(max_length=50)

class admission(models.Model):
    batchid=models.IntegerField()
    admissionno=models.AutoField(primary_key=True)
    admissiondate=models.DateField()
    emailid=models.CharField(max_length=50)