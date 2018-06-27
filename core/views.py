import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from core.forms import CaseForm


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
    if request.method == "GET":
        return render(request, "visualize.html")

    if request.method == "POST":
        print(request.POST)
        return render(request, "visualize.html")


@login_required(login_url='/')
def responsible_person_view(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, "responsible.html")

    if request.method == "POST":
        print(request.POST)
        return render(request, "responsible.html")


@login_required(login_url='/')
def new_case_view(request, *args, **kwargs):
    if request.method == "GET":
        case_form = CaseForm()
        return render(request, "case.html", {"form": case_form})
    if request.method == "POST":
        post_data = request.POST.copy()
        post_data["user"] = request.user.id
        post_data["timestamp"] = str(datetime.datetime.now())
        form_data = CaseForm(post_data)
        if form_data.is_valid():
            form_data.save()
            return HttpResponseRedirect("/dashboard/")
        return render(request, "case.html", {"form": form_data})
