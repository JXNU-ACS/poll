__author__ = 'kdwycz'

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^index/$', views.index),
    url(r'^logout/$', views.logout),
]