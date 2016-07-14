from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^page(?P<page>[0-9]+)/$', views.index, name='shop-index'),
    url(r'^', views.index, name='shop'),
]
