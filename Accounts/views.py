from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from Accounts.forms import CreateUserForm, LoginForm

class RegistrationView(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'form_registration.html', {'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/')
        return render(request, 'form_registration.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'form_login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                redirect_url = request.GET.get('next', '/')
                return redirect(redirect_url)
        return render(request, 'form_login.html', {'form': form})


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
