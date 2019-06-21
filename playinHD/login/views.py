from django.shortcuts import render

# Create your views here.
from .models import *
from bs4 import BeautifulSoup
import time
import datetime
import requests
from django.shortcuts import render,redirect,reverse,HttpResponse
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
import json
import time
import pymongo
def mylogin(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def collect_news():
    # 导入相关的模块
    url = "https://pacaio.match.qq.com/irs/rcd?cid=137&token=d0f13d594edfc180f5bf6b845456f3ea&id=&ext=top&page=0&expIds=&callback=__jp1"
    # 腾讯新闻的首页网址
    web_data = requests.get(url)  # 获取文本信息
    soup = BeautifulSoup(web_data.text, "lxml")  # 对获取到的文本信息进行解析
    data = str(soup)
    for i in range(0, len(data)):
        if data[i] == '(':
            break
    j = len(data) - 1
    while j > 0:
        if data[j] == ')':
            break
        else:
            j -= 1
    nowdata = data[i + 1:j]
    newdata = json.loads(nowdata)
    title = []
    titlelink = []
    img = []
    for m in newdata['data']:
        title.append(m['title'])
        titlelink.append(m['vurl'])
        img.append(m['bimg'])
    return title,titlelink,img
def connect_mongo():
    client=pymongo.MongoClient(host="localhost",port=27017)
    db=client.playinhd
    bus=db.bus.find({})
    food=db.food.find({})
    health=db.health.find({})
    hotel=db.hotel.find({})
    kuaidi=db.kuaidi.find({})
    play=db.play.find({})
    shopping=db.shopping.find({})
    study=db.study.find({})
    msg=[bus,food,health,hotel,kuaidi,play,shopping,study]
    return msg
def get_information(msg,name):
    for i in range(0,len(msg)):
        for j in msg[i]:
            if name in j["title"]:
                return j,i
def deal_information(name,result,location):
    if location==1:
        information = [name, result["price"], result["addr"], result["type"], result["photo"]]
        return information
    if location==2:
        str="坚持健身的人脱了衣服一眼就看出来与众不同，浑身的肌肉仿佛宣誓着自己的力量。也给人一种强大的自信！"
        information = [name, result["price"],str , "健身", result["photo"]]
        return information
    if location==3:
        information = [name, result["price"], result["address"],"酒店",result["photo"]]
        return information
    if location==4:
        information = [name,"over 8",result["address"],"快递",result["photo"]]
        return information
    if location==5:
        information = [name,"I dont know",result["address"],"娱乐",result["photo"]]
        return information
    if location==6:
        information=[name,"over 0",result["address"],"购物",result["photo"]]
        return information
    if location==7:
        information=[name,"free",result["address"],"学校",result["photo"]]
        return information
def store_information(atitle):
    msg = connect_mongo()
    result,location= get_information(msg, atitle)
    #information={"name":name,"price":result["price"],"address":result["addr"],"type":result["type"],"photo":result["photo"]}
    # if request.POST.get('name'):
    informations=deal_information(atitle,result,location)
    #     name=request.POST.get('name')
    #print(str(name)+"wocaonima")
    return informations
def index_check(request):
    userphone=request.POST.get('username')
    password=request.POST.get('password')
    if users.objects.filter(userphone=userphone,password=password):
        usersession=users.objects.get(userphone=userphone,password=password)
        request.session['username']=usersession.username
        request.session['Userphone']=usersession.userphone
        request.session.set_expiry(0)
        title=[]
        titlelink=[]
        img=[]
        username=usersession.username
        comments=comment.objects.filter(username=username).order_by("-id")
        count=0
        result=[]
        for i in comments:
            if count==5:
                break
            else:
                if i.storename in result:
                    continue
                else:
                    result.append(i.storename)
                    count+=1
        title,titlelink,img=collect_news()
        return render(request,'main.html',{"usersession":request.session['username'],"title":title,"titlelink":titlelink,"img":img,'mylook':result})
    else:
        messages.success(request, "账号或密码不正确！")
        return render(request, 'index.html')
def register_check(request):
    userphone1=request.POST.get('username')
    username=request.POST.get('myname')
    password=request.POST.get('password')
    if not users.objects.filter(userphone=userphone1):
        if not users.objects.filter(username=username):
            users.objects.create(userphone=userphone1,username=username,password=password)
            messages.success(request, "注册成功！")
            return render(request, 'index.html')
    else:
        messages.success(request, "注册失败！")
        return render(request,'register.html')
def get_comment(atitle,informations):
    comment_information=comment.objects.filter(storename=atitle).order_by("-id")
    #result=[comment_information.username,comment_information.commenttime,comment_information.commenttext]
    for i in comment_information:
        nowtime=str(i.commenttime)
        newtime=nowtime.split("+")
        information=[i.username,newtime[0],i.commenttext]
        informations.append(information)
    return informations
def deal_comment(request):
    commenttext=request.GET.get("comment")
    atitle=request.GET.get("atitle")
    username=request.session.get("username")
    now=time.time()
    nowtime=time.localtime(now)
    newtime=time.strftime('%Y-%m-%d %H:%M:%S', nowtime)
    comment.objects.create(commenttime=newtime,commenttext=commenttext,username=username,storename=atitle)
    record.objects.create(username=username,recordtime=newtime,comment=True,feedback=False)
    informations=store_information(atitle)
    informations = get_comment(atitle,informations)
    return render(request,"store.html",{"information":informations,"username":atitle})
def Feedback(request):
    return render(request,"Feedback.html")
def deal_Feedback(request):
    feedbacktext=request.GET.get("Feedback");
    username = request.session.get("username")
    now = time.time()
    nowtime = time.localtime(now)
    newtime = time.strftime('%Y-%m-%d %H:%M:%S', nowtime)
    feedback.objects.create(backtime=newtime,backtext=feedbacktext,username=username)
    record.objects.create(username=username, recordtime=newtime, comment=False, feedback=True)
    return render(request,"Feedback.html")
def return_main(request):
    title = []
    titlelink = []
    img = []
    title, titlelink, img = collect_news()
    return render(request, 'main.html',{"usersession": request.session['username'], "title": title, "titlelink": titlelink, "img": img})
def mypage(request):
    username=request.session['username']
    return render(request,'mypage.html',{'username':username})
def id_mypage(request):
    username=request.session['username']
    myinformation=users.objects.filter(username=username)
    userphone="电话："+myinformation[0].userphone
    myname="昵称："+username
    password="密码："+myinformation[0].password
    information=[userphone,myname,password]
    return JsonResponse(information,safe=False)
def comment_mypage(request):
    username=request.session['username']
    myinformation=comment.objects.filter(username=username)
    result=[]
    count=1
    for i in myinformation:
        nowtime = str(i.commenttime)
        newtime = nowtime.split("+")
        Time="时间："+newtime[0]
        mycomment="评论："+i.commenttext
        storename="商家："+i.storename
        result.append([count,Time,mycomment,storename])
        count+=1
    return JsonResponse(result,safe=False)
def feedback_mypage(request):
    username=request.session['username']
    myinformation = feedback.objects.filter(username=username)
    result = []
    count=0
    for i in myinformation:
        nowtime = str(i.backtime)
        newtime = nowtime.split("+")
        Time = "时间：" + newtime[0]
        myfeedback = "评论：" + i.backtext
        result.append([count,Time, myfeedback])
        count+=1
    return JsonResponse(result,safe=False)
def history_mypage(request):
    username=request.session['username']
    myinformation = record.objects.filter(username=username)
    result = []
    count=0
    for i in myinformation:
        nowtime = str(i.recordtime)
        newtime = nowtime.split("+")
        Time = "时间：" + newtime[0]
        mycomment=''
        myfeedback=''
        if i.comment==True:
            mycomment="已评论"
        else:
            mycomment="未评论"
        if i.feedback==True:
            myfeedback="已反馈"
        else:
            myfeedback="未反馈"
        result.append([count,Time, mycomment,myfeedback])
        count+=1
    return JsonResponse(result, safe=False)
def delete_comment(request):
    local=request.GET.get('nowlocal')
    username=request.session['username']
    comment.objects.filter(id=int(local)).delete()
    myinformation = comment.objects.all()
    count=1
    for i in myinformation:
        i.id=count
        count+=1
        i.save()
    messages.success(request, "删除成功")
    return render(request,"mypage.html",{"username":username})
def change_passwd(request):
    password1=request.GET.get("password1")
    password2=request.GET.get("password2")
    username=request.session['username']
    if users.objects.filter(username=username,password=password1):
        myinformation=users.objects.filter(username=username)
        for i in myinformation:
            i.password=password2
            i.save()
        return render(request,"index.html")
    else:
        messages.success(request,"密码验证失败")
        return render(request,"mypage.html",{"username":username})