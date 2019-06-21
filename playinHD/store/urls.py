from django.contrib import admin
from django . urls import include ,path,re_path
from django.views import static ##新增
from django.conf import settings ##新增
from django.conf.urls import url ##新增
from django.urls import path
from django.conf.urls import url,include
from . import views
urlpatterns = [
    re_path('store', views.store_information, name='store'),
]