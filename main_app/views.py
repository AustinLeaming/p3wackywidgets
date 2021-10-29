from django.http import response
from django.shortcuts import redirect, render
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView, DeleteView
from .models import Todo
from .forms import TodoForm
# Define the home view

class TodoDelete(DeleteView):
    model = Todo
    success_url = '/'
        
class TodoCreate(CreateView):
    model = Todo
    fields = '__all__'

def home(request):
    todo = Todo.objects.all()
    todo_form = TodoForm()
    return render(request, 'home.html', {'todo': todo, 'todo_form': todo_form})