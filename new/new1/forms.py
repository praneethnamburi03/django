from django import forms
from .models import student
from django.forms import ModelForm

class studentform(ModelForm):
    class Meta:
        model=student
        fields=['id','name','age','marks','pics']
    