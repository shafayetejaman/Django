from django.shortcuts import render, redirect
from .forms import Register
from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy


# Create your views here.
@method_decorator(login_required, name="dispatch")
class UserSignupView(CreateView):
    template_name = "authenticate/signup.html"
    success_url = reverse_lazy("login")
    form_class = Register

    def form_valid(self, form):
        messages.success(self.request, "Account Created Successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Account Creation Failed!")
        return super().form_invalid(form)


class UserLoginView(LoginView):
    template_name = "authenticate/login.html"

    def get_success_url(self):
        return reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Logged In Successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Login Failed!")
        return super().form_invalid(form)


@login_required()
def user_logout(request):
    logout(request)
    return redirect("login")


@method_decorator(login_required, name="dispatch")
class PasswordChangeView(PasswordChangeView):
    template_name = "authenticate/pass_change.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, "Password Updated Successfully!")
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)
