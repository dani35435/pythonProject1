from django.urls import path
from .views import index, about, contacts, profile, LoginView, LogoutView, product

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('accounts/profile/', profile, name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('product/', product, name='product'),
]
