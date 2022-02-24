from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Studeinfo

from .models import Studeinfo
class FormInfo(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')
        widgets = {
            'username': forms.CharField(attrs={'class': 'class1'}),
            'username': forms.CharField(attrs={'class': 'class2'}),
            'username': forms.CharField(attrs={'class': 'class3'}),
        }

# class UserFormInfo(forms.ModelForm):
#     class Meta:
#         model=Studeinfo

class LoginForm(forms.Form):
    username=forms.CharField(max_length=227)
    password=forms.CharField(widget=forms.PasswordInput())
