from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here
class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'Enter Your Name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'Enter Your Email',
            }),

            'password1': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'Enter Your Password'
            }),

            'password2': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'Confirm Password'
            }),
        }