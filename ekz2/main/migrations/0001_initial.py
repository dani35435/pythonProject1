# Generated by Django 3.2.16 on 2022-12-20 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, verbose_name='название')),
                ('desc', models.TextField(blank=True, verbose_name='описание')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='фото')),
            ],
        ),
    ]
