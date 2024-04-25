from django.shortcuts import render, redirect


def home(request):
    return render(request, "base.html",{"logged": request.user.is_authenticated})