from django.db import models
from tinymce import models as tinymce_models
from django import forms
from autoslug import AutoSlugField
from django.core.validators import EmailValidator


from datetime import date
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class Todo(models.Model):
    category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    sehir = models.CharField(max_length=100)
    ulke= models.CharField(max_length=200)
    posta= models.CharField(max_length=200)
    website=models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='avatar')

class Contact(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    subject=models.TextField()

    def __str__(self):
        return self.name

