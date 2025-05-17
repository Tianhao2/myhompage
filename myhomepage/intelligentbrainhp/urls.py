"""
URL configuration for intelligentbrainhp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseNotFound

# 处理 404 的视图函数
def redirect_to_home(request, exception=None):
    return redirect('/')

# 注册 handler
handler404 = redirect_to_home

def health_check(request):
    return HttpResponse("OK")

urlpatterns = [
    path('survey/', include('survey.urls')),
    path('admin/', admin.site.urls),
    path("health/", health_check),  # 🔍 ALB healthcheck用
    path('', include('home.urls')),
]