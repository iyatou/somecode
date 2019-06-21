from django.db import models
import mongoengine
# Create your models here.
class users(models.Model):
    userphone=models.CharField(max_length=50,default="")
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
class record(models.Model):
    username=models.CharField(max_length=50,default="")
    recordtime=models.DateTimeField(null=True,auto_now=False)
    comment=models.BooleanField()
    feedback=models.BooleanField()
class comment(models.Model):
    username=models.CharField(max_length=50,default="")
    commenttime = models.DateTimeField(null=True, auto_now=False)
    commenttext=models.CharField(max_length=500)
    storename = models.CharField(max_length=50,default='')
class feedback(models.Model):
    username = models.CharField(max_length=50,default="")
    backtime=models.DateTimeField(null=True, auto_now=False)
    backtext=models.CharField(max_length=500)
