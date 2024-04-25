from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
#from .models import TodoListItem
from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task



class TaskViewSet(viewsets.MoelViewSet):

    query_set =  Task.objects.filter(delete=False)
    serializer_class = TaskSerializer




