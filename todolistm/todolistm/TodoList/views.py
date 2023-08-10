from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.
app_name = "TodoList"


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('index')
    return render(request, 'index.html')


def login_form(request):
    return render(request, 'login.html')


def forgot_password(request):
    return render(request, 'forget_password.html')


def dashboard(request):
    return render(request, 'index.html')





def layouts_without_menu(request):
    return render(request, 'without_menu.html')


def layouts_without_navbar(request):
    return render(request, 'layouts-without-navbar.html')


def layouts_container(request):
    return render(request, 'layouts-container.html')


def layouts_fluid(request):
    return render(request, 'layouts-fluid.html')


def layouts_blank(request):
    return render(request, 'layouts-blank.html')
