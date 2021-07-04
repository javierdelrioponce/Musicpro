
from django import urls
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from blogapp import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^compra', views.compra, name='compra'),
    url(r'^cuerdas', views.cuerdas, name='cuerdas'),
    url(r'^accesorios', views.accesorios, name='accesorios'),
    url(r'^amplificadores', views.amplificadores, name='amplificadores'),
    url(r'^percusion', views.percusion, name='percusion'),
    url(r'^$', views.menu, name='menu'),
    
]