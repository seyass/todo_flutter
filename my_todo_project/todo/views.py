from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    print('hi')
    return JsonResponse({"message":'hellw world'})