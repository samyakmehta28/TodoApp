from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class TodoList(models.Model):
    text = models.CharField(max_length=60)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text