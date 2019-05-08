from django.db import models
from django import forms

class Msg(models.Model):
    name = models.CharField(max_length=200)

# Create your models here.
