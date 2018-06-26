from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


from django import forms


def index_view(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/dashboard/")
    return render(request, "index.html")


def login_view(request, *args, **kwargs):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    print(user)
    if user:
        login(request, user)
        return HttpResponseRedirect("/dashboard/")
    return render(request, "index.html", {"error": "Invalid username or password"})


def logout_view(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect("/")


@login_required(login_url='/')
def dashboard_view(request, *args, **kwargs):
    return render(request, "dashboard.html")


@login_required(login_url='/')
def visualize_view(request, *args, **kwargs):
    return render(request, "visualize.html")


@login_required(login_url='/')
def new_case_view(request, *args, **kwargs):
    return render(request, "case.html")