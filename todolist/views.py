from django.shortcuts import render, redirect
from django.db.models import Q
from .models import TodoList
from .forms import TodoListForm
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    todo_items = TodoList.objects.filter(author = request.user).order_by('id')
    form = TodoListForm()
    context = {'todo_items' : todo_items, 'form' : form}
    return render(request,'todolist/index.html',context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_todo = TodoList(text=request.POST['text'], author=request.user)
        new_todo.save()
    return redirect('index')

def completedTodo(request,todo_id):
    todo = TodoList.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def deleteCompletedTodo(request):
    TodoList.objects.filter(author = request.user).filter(completed__exact=True).delete()
    return redirect('index')

def deleteAllTodo(request):
    TodoList.objects.filter(author = request.user).delete()
    return redirect('index')