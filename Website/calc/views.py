from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

def home(request):
    if request.method=='POST':
        x = Todo(work = request.POST['work'],time = request.POST['time'])
        x.save()
        return redirect('/')
    else:
        todos = Todo.objects.all()
    return render(request, 'home.html',{'todos':todos})
    