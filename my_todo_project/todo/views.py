from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
#from .models import TodoListItem
from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset =  Task.objects.filter(deleted=False)
    serializer_class = TaskSerializer




