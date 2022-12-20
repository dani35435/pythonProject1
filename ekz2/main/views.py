from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import OrderCreate


class LoginView(LoginView):
    template_name = 'main/login.html'
    success_url = reverse_lazy('main/index.html')


class LogoutView(LogoutView):
    template_name = 'main/logout.html'


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def profile(request):
    if request.method == 'POST':
        form = OrderCreate(request.POST, request.FILES)
        form.save()
        return redirect('/product')
    else:
        form = OrderCreate
    context = {'form': form}
    return render(request, 'main/profile.html', context)