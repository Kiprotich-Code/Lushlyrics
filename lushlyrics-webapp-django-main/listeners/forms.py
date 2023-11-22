from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'