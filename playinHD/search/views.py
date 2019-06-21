from django.shortcuts import render
from django.shortcuts import render,redirect,reverse,HttpResponse
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
import json
import pymongo
import re
# Create your views here.
def connect_mongo(name):
    client=pymongo.MongoClient(host="localhost",port=27017)
    db=client.playinhd
    collection=db.hotel.find({})
    msg=["bus","food","health","hotel","kuaidi","play","shopping","study"]
    result=[]
    for i in msg:
        for m in db[i].find({"title":re.compile(name)}):
            a=[m['title'],m['photo']]
            result.append(a)
    if len(result)<16:
        for z in range(len(result),16):
            for r in collection:
                a=[r["title"],r["photo"]]
                result.append(a)
    return result
def search_information(request):
    name=request.GET.get("storename")
    result=connect_mongo(name)
    print(result)
    count=1
    for i in range(0,len(result)):
        if i%10==0:
            if i==0:
                result[i].insert(0, count)
            else:
                count+=1
                result[i].insert(0,count)
        else:
            result[i].insert(0,count)
    print(result)
    return render(request,'search_information.html',{"result":result})
def search_play(request):
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client.playinhd
    collection = db.play
    msg = collection.find({})
    title = []
    photo = []
    information=[]
    count = 0
    for i in msg:
        if count == 10:
            break
        if int(i["ratenumber"]) > 900 and i["photo"] != "":
            title.append(i["title"])
            photo.append(i["photo"])
            count += 1
    information.append(title)
    information.append(photo)
    return JsonResponse(information,safe=False)
def search_shopping(request):
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client.playinhd
    collection = db.shopping
    msg = collection.find({})
    title = []
    photo = []
    information = []
    count = 0
    for i in msg:
        if count == 10:
            break
        if int(i["ratenumber"]) > 900 and i["photo"] != "":
            title.append(i["title"])
            photo.append(i["photo"])
            count += 1
    information.append(title)
    information.append(photo)
    return JsonResponse(information, safe=False)
def search_food(request):
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client.playinhd
    collection = db.food
    msg = collection.find({})
    title = []
    photo = []
    information = []
    count = 0
    for i in msg:
        if count == 10:
            break
        if int(i["ratenumber"]) > 1000 and i["photo"] != "":
            title.append(i["title"])
            photo.append(i["photo"])
            count += 1
    information.append(title)
    information.append(photo)
    return JsonResponse(information, safe=False)
def search_hotel(request):
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client.playinhd
    collection = db.hotel
    msg = collection.find({})
    title = []
    photo = []
    information = []
    count = 0
    for i in msg:
        if count == 10:
            break
        if float(i["rate"]) == 5.0 and i["photo"] != "":
            title.append(i["title"])
            photo.append(i["photo"])
            count += 1
    information.append(title)
    information.append(photo)
    return JsonResponse(information, safe=False)
def search_health(request):
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client.playinhd
    collection = db.health
    msg = collection.find({})
    title = []
    photo = []
    information = []
    count = 0
    for i in msg:
        if count == 10:
            break
        if int(i["ratenumber"]) > 1000 and i["photo"] != "":
            title.append(i["title"])
            photo.append(i["photo"])
            count += 1
    information.append(title)
    information.append(photo)
    return JsonResponse(information, safe=False)
def search_study(request):
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client.playinhd
    collection = db.study
    msg = collection.find({})
    title = []
    photo = []
    information = []
    count = 0
    for i in msg:
        if count == 10:
            break
        if i["photo"] != "" and "哈尔滨" in i["title"]:
            title.append(i["title"])
            photo.append(i["photo"])
            count += 1
    information.append(title)
    information.append(photo)
    return JsonResponse(information, safe=False)
def search_kuaidi(request):
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client.playinhd
    collection = db.kuaidi
    msg = collection.find({})
    title = []
    photo = []
    information = []
    count = 0
    for i in msg:
        if count == 10:
            break
        if i["photo"] != "":
            title.append(i["title"])
            photo.append(i["photo"])
            count += 1
    information.append(title)
    information.append(photo)
    print(information)
    return JsonResponse(information, safe=False)
def search_bus(request):
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client.playinhd
    collection = db.bus
    msg = collection.find({})
    title = []
    photo = []
    information = []
    count = 0
    for i in msg:
        if count == 10:
            break
        title.append(i["title"])
        photo.append("http://08imgmini.eastday.com/mobile/20180920/20180920000517_b446c0d25823cad38eb1c79d11eac105_1.jpeg")
        count += 1
    information.append(title)
    information.append(photo)
    return JsonResponse(information, safe=False)