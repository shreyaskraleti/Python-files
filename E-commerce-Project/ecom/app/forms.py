from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from . models import Customer
 
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':
    'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    'autocomplete':'current-password', 'class':'form-control'}))
 
class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
   
    class Meta:
        model = User
        fields = ['username',  'password1', 'password2','email',]
 
class MyPasswordResetForm(PasswordChangeForm):
    pass
class CustomProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'mobile', 'state', 'zipcode']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'locality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your locality'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your mobile number'}),
            'state': forms.Select(attrs={'class': 'form-control'}),  # Assuming state is a choice field
            'zipcode': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your ZIP code'}),
        }
