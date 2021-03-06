"""livechat URL Configuration

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
from django.urls import path, include
from redischatapp import views as redischatviews
from mariachatapp import views as mariachatviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maria/home/', mariachatviews.home, name='mariahome'),
    path('redis/home/', mariachatviews.home, name='redishome'),

    path('redis/login/', redischatviews.redislogin, name='redislogin'),
    path('redis/logout/', redischatviews.redislogout, name='redislogout'),
    path('redis/register/', redischatviews.redisregister, name='redisregister'),

    path('maria/login/', mariachatviews.marialogin, name='marialogin'),
    path('maria/logout/', mariachatviews.marialogout, name='marialogout'),
    path('maria/register/', mariachatviews.mariaregister, name='mariaregister'),
]
