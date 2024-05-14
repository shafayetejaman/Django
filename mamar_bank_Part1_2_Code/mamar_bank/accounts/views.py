from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView

class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake


class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')


@login_required()
def UserLogout(request):
    logout(request)
    return redirect("login")


class UserBankAccountUpdateView(UpdateView):
    template_name = "accounts/profile.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user
