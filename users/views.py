# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm, UserProfileUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# User Registration View
class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

# User Login View
class UserLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'users/login.html', {'form': form})

# User Logout View
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

# User Profile Update View
class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'
    form_class = UserProfileUpdateForm
    model = User
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
