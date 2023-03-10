from django import forms

from .models import Product


class OrderCreate(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'desc', 'photo')
        enctype = "multipart/form-data"