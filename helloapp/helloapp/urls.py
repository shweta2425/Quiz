"""helloapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from howdy.views import *
# from howdy.views import CreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^', include('howdy.urls')),
    path('', home),
    path('2/', nav_view, name="template2"),
    path('', home, name="template1"),
    url(r'^short_exam/$', CreateView.as_view(), name="create"),
]
