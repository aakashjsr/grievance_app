import datetime, json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from core.forms import CaseForm, ResponsibilityForm
import core.models as models


def index_view(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/dashboard/")
    return render(request, "index.html")


def login_view(request, *args, **kwargs):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return HttpResponseRedirect("/dashboard/")
    return render(request, "index.html", {"error": "Invalid username or password"})


def logout_view(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect("/")


@login_required(login_url='/')
def dashboard_view(request, *args, **kwargs):
    return render(request, "dashboard.html", {"projects": request.user.projects.all()})


@login_required(login_url='/')
def project_view(request, project_id, *args, **kwargs):
    project = models.Project.objects.get(id=project_id)
    return render(request, "project.html", {"project": project, "cases": project.cases.all()})


@login_required(login_url='/')
def case_view(request, case_id, *args, **kwargs):
    case = models.Case.objects.get(id=case_id)
    return render(request, "case.html", {"case": case})


@login_required(login_url='/')
def visualize_view(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, "visualize.html")

    if request.method == "POST":
        return render(request, "visualize.html")


@login_required(login_url='/')
def responsible_person_view(request, *args, **kwargs):
    if request.method == "POST":
        post_data = request.POST.copy()

        post_data["added_by"] = request.user.id
        form_data = ResponsibilityForm(post_data)
        if form_data.is_valid():
            form_data.save()
            project = models.Project.objects.get(id=post_data.get("project_id"))
            case_form = CaseForm(initial=json.loads(post_data.get("saved")))
            responsible_data = {}
            for data in models.ResponsibleEntity.objects.all():
                responsible_data[data.id] = {"organization": data.organisation, "position": data.position,
                                             "site": data.site}
            return render(request, "new_case.html", {
                "form": case_form, "project": project, "case_id": project.cases.count() + 1,
                "responsible_data": responsible_data
            })
        return render(request, "new_responsible.html", {"form": form_data})


@login_required(login_url='/')
def new_case_view(request, *args, **kwargs):
    if request.method == "GET":
        project = models.Project.objects.get(id=request.GET.get("project_id"))
        case_form = CaseForm()
        responsible_data = {}
        for data in models.ResponsibleEntity.objects.all():
            responsible_data[data.id] = {"organization": data.organisation, "position": data.position, "site": data.site}
        return render(request, "new_case.html", {
            "form": case_form, "project": project, "case_id": project.cases.count() + 1,
            "responsible_data": responsible_data
        })
    if request.method == "POST":
        post_data = request.POST.copy()
        post_data["user"] = request.user.id
        post_data["timestamp"] = str(datetime.datetime.now())
        post_data["case_id"] = models.Project.objects.get(id=post_data["project"]).cases.count() + 1
        form_data = CaseForm(post_data)
        if form_data.is_valid():
            form_data.save()
            return HttpResponseRedirect("/dashboard/")
        return render(request, "new_case.html", {"form": form_data})
