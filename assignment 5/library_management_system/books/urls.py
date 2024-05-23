"""
URL configuration for car_sales project.

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
from .views import DetailPostView, CreatePostView, DeletePostView, home, UpdatePostView, buy_book

urlpatterns = [
    path("add/", CreatePostView.as_view(), name="add"),
    path("detail/<int:id>/<slug:book_slug>/", DetailPostView.as_view(), name="detail"),
    path("update/<int:id>/", UpdatePostView.as_view(), name="update"),
    path("delete/<int:id>/", DeletePostView.as_view(), name="delete"),
    path("buy/<int:id>/", buy_book, name="buy"),
    path("group_by/<slug:category_slug>", home, name="group_by"),
]