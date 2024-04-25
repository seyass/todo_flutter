from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import TodoListItem

# Create your views here.
def home(request):
    print('hi')
    return JsonResponse({"message":'hellw world'})


# adding task function
def add_task(request):

    # adding task
    if request.POST:
        
        task = request.POST['task']

        # validating task content
        if len(task.strip()) <= 2:
            
            # return failed respond
            return JsonResponse({'message':'failed'})
        TodoListItem.objects.create(task=task)

        # return success message
        return JsonResponse({'messsage':'success'})
    return JsonResponse({'message':'add_task url'})