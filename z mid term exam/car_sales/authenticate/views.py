from django.shortcuts import render, redirect
from .forms import Register
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# @method_decorator(login_required, name="dispatch")


class UserSignupView(CreateView):
    template_name = "authenticate/signup.html"
    success_url = reverse_lazy("login")
    form_class = Register

    def form_valid(self, form):
        messages.success(self.request, "Account Created Successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Account Creation Failed!")
        return super().form_invalid(form)


@method_decorator(login_required, name="dispatch")
class UserLoginView(LoginView):
    template_name = "authenticate/login.html"

    def get_success_url(self):
        return reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Logged In Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Login Failed!")
        return super().form_invalid(form)


@login_required()
def user_logout(request):
    logout(request)
    return redirect("login")
