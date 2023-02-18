# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=255,
        label="username",
        widget=forms.TextInput(attrs={
            'class': 'w-100 form-control',
            'placeholder': 'username',
            'id': 'a'
        }
        )
    )
    email = forms.CharField(
        max_length=255,
        label="email",
        widget=forms.TextInput(attrs={
            'class': 'w-100 form-control',
            'placeholder': 'email',
            'id': 'b'
        }
        )
    )
    password1 = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-100 form-control',
            'placeholder': 'password1',
            'id': 'b'
        }
        )
    )
    password2 = forms.CharField(
        label="repeat password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-100 form-control',
            'placeholder': 'repeat password',
            'id': 'c'

        }
        )
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
