from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
def mylogin(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def register_check(request):
    return HttpResponse('asfdasdf')