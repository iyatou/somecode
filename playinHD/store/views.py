#encoding=utf-8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render,redirect,reverse,HttpResponse
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
import json
import pymongo
from login.models import comment
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
            if name == j["title"]:
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
        information = [name,"8up",result["address"],"快递",result["photo"]]
        return information
    if location==5:
        information = [name,"none",result["address"],"娱乐",result["photo"]]
        return information
    if location==6:
        information=[name,"0up",result["address"],"购物",result["photo"]]
        return information
    if location==7:
        information=[name,"free",result["address"],"学校",result["photo"]]
        return information
def get_comment(atitle,informations):
    comment_information=comment.objects.filter(storename=atitle).order_by("-id")
    #result=[comment_information.username,comment_information.commenttime,comment_information.commenttext]
    for i in comment_information:
        nowtime=str(i.commenttime)
        newtime=nowtime.split("+")
        information=[i.username,newtime[0],i.commenttext]
        informations.append(information)
    return informations
def store_information(request):
    name=request.GET.get('name')
    msg = connect_mongo()
    result,location= get_information(msg, name)
    #information={"name":name,"price":result["price"],"address":result["addr"],"type":result["type"],"photo":result["photo"]}
    # if request.POST.get('name'):
    information=deal_information(name,result,location)
    #     name=request.POST.get('name')
    #print(str(name)+"wocaonima")
    username=request.session.get('username')
    informations=get_comment(name,information)
    return render(request,"store.html",{"information":informations,"username":username})