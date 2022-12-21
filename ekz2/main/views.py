from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import OrderCreate
from .models import Product


class LoginView(LoginView):
    template_name = 'main/login.html'
    success_url = reverse_lazy('main/index.html')


class LogoutView(LogoutView):
    template_name = 'main/logout.html'


def index(request):
    product = Product.objects.all()
    return render(request, 'main/index.html', {'product': product})


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


@login_required
def profile(request):
    if request.method == 'POST':
        form = OrderCreate(request.POST, request.FILES)
        form.save()
        return redirect('main:index')
    else:
        form = OrderCreate
    context = {'form': form}
    return render(request, 'main/profile.html', context)


def product(request):
    res = Product.objects.all()
    return render(request, 'main/product.html', {'res': res})