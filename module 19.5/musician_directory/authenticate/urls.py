"""
URL configuration for project_18_5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import user_signup, user_login, home, user_logout, password_change,password_change_without , UserLoginView, UserLogoutView


urlpatterns = [
    path("signup/", user_signup, name="signup"),
    # path("login/", user_login, name="login"),
    path("login/", UserLoginView.as_view(), name="login"),
    # path("logout/", user_logout, name="logout"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("", home, name="home"),
    path("pass_change/", password_change, name="pass_change"),
    path("pass_forgot/", password_change_without, name="pass_forgot"),
]
