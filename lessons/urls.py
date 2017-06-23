from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.LessonHome.as_view(), name='lessons'),
    url(r'^ssl20/', views.ssl20.as_view(), name='ssl20'),
]
