from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView


class UserRegistrationView(CreateView):
    template_name = "accounts/user_registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
    
        login(self.request, self.user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')


class UserBankAccountUpdateView(UpdateView):
    template_name = "accounts/profile.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user
