# chat/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    #if request.user.is_anonymous:
    #      return redirect("/login")
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'index.html', {'users': users})

#@login_required
def chat(request, username):
    if request.user.is_anonymous:
          return redirect("/login")
    other_user = User.objects.get(username=username)
    return render(request, 'chat.html', {'other_user': other_user})

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('/login')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def chat_room(request, username):
    if request.user.is_anonymous:
          return redirect("/login")
    other_user = get_object_or_404(User, username=username)
    if request.user.username < other_user.username:
        room_name = f'{request.user.username}_{other_user.username}'
    else:
        room_name = f'{other_user.username}_{request.user.username}'
    return render(request, 'chat.html', {
        'room_name': room_name,
        'other_user': other_user
    })
def account(request):
    return render(request,'account.html')
