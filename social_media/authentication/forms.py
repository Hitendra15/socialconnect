from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    password2 = forms.CharField(widget=forms.PasswordInput(render_value=True),label='Confirm Password')
    class Meta:
        model = User
        fields = ('username','first_name','email','last_name','password1','password2')
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}