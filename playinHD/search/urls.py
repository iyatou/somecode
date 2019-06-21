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
    path(r'search_play', views.search_play, name='search_play'),
    path(r'search_shopping', views.search_shopping, name='search_shopping'),
    path(r'search_food', views.search_food, name='search_food'),
    path(r'search_hotel', views.search_hotel, name='search_hotel'),
    path(r'search_health', views.search_health, name='search_health'),
    path(r'search_study', views.search_study, name='search_study'),
    path(r'search_bus', views.search_bus, name='search_bus'),
    path(r'search_kuaidi', views.search_kuaidi, name='search_kuaidi'),
    path(r'^search_information',views.search_information,name='search_information'),
]
