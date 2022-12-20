from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254, verbose_name='название', blank=True)
    desc = models.TextField(verbose_name='описание', blank=True)
    photo = models.ImageField(verbose_name='фото', blank=True)