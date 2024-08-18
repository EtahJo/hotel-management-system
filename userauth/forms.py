from django import forms
from django.contrib.auth.forms import UserCreationForm

from userauth.models import User,Profile

class UserRgisterForm(UserCreationForm):
    full_name= forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Full name"}))
    username= forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter username"}))
    email= forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter email"}))
    phone= forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Phone Number"}))
    password1= forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Password"}))
    password2= forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Again"}))
    class Meta:
        model = User
        fields =['full_name',"username","email",'phone', 'password1','password2']