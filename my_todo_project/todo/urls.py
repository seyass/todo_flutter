from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home,name='home'), # url 
    path('add_task/',views.add_task,name='add_task'), # url for adding task

]


