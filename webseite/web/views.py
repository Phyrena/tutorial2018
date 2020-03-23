from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm, LoginForm
from .models import Todo

from .models import Post
from django.utils import timezone

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'web/base.html')


def register_view(request):
    register_form = RegisterForm()
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            email = register_form.cleaned_data['email']
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('', kwargs={'username': request.user.username}))
    return render(request, 'web/register.html', {'register_form': register_form})


def login_view(request):
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
    return render(request, 'web/login.html', {'login_form': login_form})




def logout_view(request):
    logout(request)
    return redirect(reverse('web:index'))


def spiel_Website_view(request):
    return render(request, 'base.html')


def klassen_view(request):
    return render(request, 'web/klassen.html')



def downloads_view(request):
    return render(request, 'web/downloads.html')


def forum_view(request):
    return render(request, 'web/forum.html')

def team_view(request):
    return render(request, 'web/team.html')


def neuste_beiträge_view(request):
    return render(request, 'web/neuste_beiträge.html')



def forum_post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'web/forum_post_list.html', {'posts': posts})



#To-Do-Liste
@csrf_exempt
def to_do_list_view(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'web/to_do_list.html', {
        "todo_items": todo_items
    })
#To-Do-Liste
def add_todo(request):
    print(request.POST)
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = Todo.objects.create(added_date=current_date, text=content)
    print(current_date)
    print(content)
    print(created_obj)
    print(created_obj.id)
    length_of_todos = Todo.objects.all().count()
    print(length_of_todos)
    return HttpResponseRedirect('web/to_do_list.html')





