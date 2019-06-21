"""playinHD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
urlpatterns = [
    path(r'', views.mylogin, name='login'),
    path(r'register/',views.register,name='register'),
    path(r'register_check/',views.register_check,name='register_check'),
    path(r'index_check/',views.index_check,name='index_check'),
    path(r'deal_comment',views.deal_comment,name='deal_comment'),
    path(r'Feedback',views.Feedback,name='Feedback'),
    path(r'deal_Feedback',views.deal_Feedback,name='deal_Feedback'),
    path(r'return_main',views.return_main,name='return_main'),
    path(r'mypage',views.mypage,name='mypage'),
    path(r'id_mypage',views.id_mypage,name='id_mypage'),
    path(r'coment_mypage',views.comment_mypage,name='comment_mypage'),
    path(r'feedback_mypage',views.feedback_mypage,name='feedback_mypage'),
    path(r'history_mypage',views.history_mypage,name='history_mypage'),
    path(r'delete_comment',views.delete_comment,name='delete_comment'),
    path(r'change_passwd',views.change_passwd,name='change_passwd'),
]
