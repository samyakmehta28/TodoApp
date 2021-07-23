from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class TodoList(models.Model):
    text = models.CharField(max_length=60)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="todo_created_by", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text