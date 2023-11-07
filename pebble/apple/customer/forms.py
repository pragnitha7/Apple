from django import forms
from .models import user_profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class userregisterform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

class userprofileform(forms.ModelForm):
    class Meta:
        model=user_profile
        fields=['profile_pic','firstname','lastname','phonenumber','email','address','city','state','country']

