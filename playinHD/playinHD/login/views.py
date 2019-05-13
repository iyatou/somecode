from django.shortcuts import render

# Create your views here.
from .models import users
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib import messages
import json
def mylogin(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def register_check(request):
    userphone1=request.POST.get('username')
    username=request.POST.get('myname')
    password=request.POST.get('password')
    ret = {"status": "NG", "msg": None}
    if not users.objects.filter(userphone=userphone1):
        users.objects.create(userphone=userphone1,username=username,password=password)
        ret["status"]="NG"
        ret["msg"]="注册成功！"
        return HttpResponse(json.dumps(ret))
    else:
        ret["status"] = "QG"
        ret["msg"] = "注册失败！"
        return HttpResponse(json.dumps(ret))






