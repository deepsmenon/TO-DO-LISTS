from django.shortcuts import render, redirect,get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()  # Get all tasks
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()  # This will trigger the save() method logic and set the completed_date
    return redirect('task_list') 
