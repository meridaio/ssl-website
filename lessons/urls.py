from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.LessonHome.as_view(), name='lessons'),
    url(r'^ssl20scenario1/', views.ssl20.as_view(), name='ssl20'),
    url(r'^ssl20alt1/', views.ssl20Alt1.as_view(), name='ssl20alt1'),
    url(r'^ssl20s2/', views.ssl20S2.as_view(), name = 'ssl20s2'),
    url(r'^ssl20s3/', views.ssl20S3.as_view(), name = 'ssl20s3'),
    url(r'^ssl3s1/', views.ssl3S1.as_view(), name='ssl3s1')
]
