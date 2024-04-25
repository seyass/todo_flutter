from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"tasks",views.TaskViewSet)


urlpatterns = [

    #path('home/',views.home,name='home'), # url 
    #path('add_task/',views.add_task,name='add_task'), # url for adding task
    path('',include(router.urls))


]

