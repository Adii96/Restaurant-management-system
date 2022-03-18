from django import forms
from django.contrib.auth.models import User

class CreateUserForm(forms.ModelForm):


     class Meta:
         model = User
         fields = ['username', 'first_name', 'last_name', 'email', 'password']
         widgets = {
             'username': forms.TextInput(attrs={'class': 'name_input'}),
             'first_name': forms.TextInput(attrs={'class': 'name_input'}),
             'last_name': forms.TextInput(attrs={'class': 'name_input'}),
             'email': forms.TextInput(attrs={'class': 'name_input'}),
             'password': forms.PasswordInput(attrs={'class': 'name_input'}),
         }



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'name_input'}), label='Nazwa Użytkownika')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'name_input'}),label='Hasło')