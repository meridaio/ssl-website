from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.LessonHome.as_view(), name='lessons'),
    url(r'^ssl20scenario1/', views.ssl20.as_view(), name='ssl20'),
    url(r'^ssl20alt1/', views.ssl20Alt1.as_view(), name='ssl20alt1'),
]
