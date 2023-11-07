from cgitb import grey
from dataclasses import fields
from django import forms
from .models import foodItem


class foodAddForm(forms.ModelForm):
    class Meta:
        model=foodItem
        fields=['food_name','description','price','image','is_available']

class foodEditForm(forms.ModelForm):
    class Meta:
        model=foodItem
        fields=['food_name','description','category','price','image','is_available']
