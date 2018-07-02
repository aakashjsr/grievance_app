"""grievance_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import *
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index_view, name="home"),
    url(r'^login/', login_view, name="login"),
    url(r'^project/(?P<project_id>\d+)/$', project_view, name="project"),
    url(r'^case/(?P<case_id>\d+)/$', case_view, name="case"),
    url(r'^logout/', logout_view, name="logout"),
    url(r'^new-case/', new_case_view, name="new_case"),
    url(r'^visualize/', visualize_view, name="visualize"),
    url(r'^responsible-person/', responsible_person_view, name="responsible"),
    url(r'^dashboard/', dashboard_view, name="dashboard"),
]
