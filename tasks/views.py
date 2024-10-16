from django.shortcuts import render, redirect,get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()  
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()  
        description = request.POST.get('description', '').strip()  

        if title:  
            title = title.capitalize() 
            Task.objects.create(title=title, description=description)
            return redirect('task_list')
        else:
            
            error_message = "Title cannot be empty."
            return render(request, 'tasks/add_task.html', {'error_message': error_message})

    return render(request, 'tasks/add_task.html')


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()  
    return redirect('task_list') 
from django.shortcuts import redirect

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
