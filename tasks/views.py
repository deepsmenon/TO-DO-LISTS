from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from .models import Task
import requests


def task_list(request):
    tasks = Task.objects.all()
    quote = get_motivational_quote()  # Call without 'request'
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'quote': quote})
    
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'quote': quote})
def add_task(request):
    if request.method == 'POST':
        print("Form submitted!")  # Debug output
        title = request.POST.get('title', '').strip()  
        description = request.POST.get('description', '').strip()  
        print(f"Title: '{title}', Description: '{description}'")  # Debug output

        if title:  
            title = title.capitalize() 
            try:
                Task.objects.create(title=title, description=description)
                print("Task created successfully")  # Debug output
                return redirect('task_list')
            except Exception as e:
                print(f"Error creating task: {e}")  # Print any errors
                error_message = "Failed to create task. Please try again."
                return render(request, 'tasks/add_task.html', {'error_message': error_message})
        else:
            error_message = "Title cannot be empty."
            return render(request, 'tasks/add_task.html', {'error_message': error_message})

    return render(request, 'tasks/add_task.html')


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()  # This will call the save method in your model
    return redirect('task_list') 

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()  # Delete the task directly
    return redirect('task_list')  # Redirect back to the task list
    
def get_motivational_quote():
    url = 'https://zenquotes.io/api/random'
    try:
        response = requests.get(url)
        response.raise_for_status()
        quote_data = response.json()
        quote = quote_data[0]['q']  # Extracting quote text
        author = quote_data[0]['a']  # Extracting author
        return {'quote': quote, 'author': author}  # Return the quote and author as a dictionary
    except requests.exceptions.RequestException:
        return {'error': 'Could not fetch quote'}  # Handle the error