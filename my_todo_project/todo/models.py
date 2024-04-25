from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# user's todo list
class UserTodoList(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE) # user 
    created_at = models.DateField(auto_now_add=True) # user todo list created
    
    def __str__(self):
        return self.user.username

# todolist items
class TodoListItem(models.Model):

    user = models.ForeignKey(UserTodoList,on_delete=models.CASCADE) # user
    task = models.CharField(max_length=100) # task contents
    created_at = models.DateField(auto_now_add=True) # date created
    is_active = models.BooleanField(default=True) # for soft delete

    def __str__(self):
        return self.task

