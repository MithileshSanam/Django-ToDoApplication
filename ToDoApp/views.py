from django.shortcuts import render,redirect
from ToDoApp.models import ToDoModel
# Create your views here.

def generate(request,check_id):
    todo_items= ToDoModel.objects.order_by('-id')
    return render(request,'home.html',{'todo_items':todo_items,'check_id':check_id})

def home(request):
    return generate(request,0)

def delete_task(request,todo_id):
    if request.method !='POST':
        return redirect('home')
    ToDoModel.objects.get(id=todo_id).delete()
    return redirect('home')

def edit_task(request,todo_id):
    if request.method !='POST':
        return redirect('home')
    return generate(request,todo_id)

def update_task(request,todo_id):
    if request.method !='POST':
        return redirect('home')
    if 'edit_task_submit' in request.POST:
        todo_obj = ToDoModel.objects.get(id=todo_id)
        newtask = request.POST.get('editedtext')
        todo_obj.task = newtask
        todo_obj.save()
        return redirect('home')
    elif 'cancel_task_submit' in request.POST:
        return redirect('home')


def add_task(request):
    if request.method !='POST':
        return redirect('home')
    task = request.POST.get('newtask')
    todo = ToDoModel(task=task)
    todo.save()
    return redirect('home')
