from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib.auth.models import User    

class CreateUserForm(UserCreationForm):
    class Meta:
        
        model = User
        fields = ['username','email','first_name','password1','password2']


class LoginForm(AuthenticationForm):
    
    username = forms.CharField()
    password = forms.CharField()


