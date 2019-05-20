from django.db import models

# Create your models here.
class users(models.Model):
    userphone=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
class record(models.Model):
    userphone=models.ForeignKey(users,on_delete=models.CASCADE,default='')
    recordtime=models.DateTimeField(null=True,auto_now=False)
    comment=models.BooleanField()
    feedback=models.BooleanField()
class comment(models.Model):
    userphone=models.ForeignKey(users,on_delete=models.CASCADE,default='')
    commenttime = models.DateTimeField(null=True, auto_now=False)
    commenttext=models.CharField(max_length=500)
class feedback(models.Model):
    userphone = models.ForeignKey(users, on_delete=models.CASCADE, default='')
    backtime=models.DateTimeField(null=True, auto_now=False)
    backtext=models.CharField(max_length=500)