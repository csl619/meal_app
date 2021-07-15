from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.layout import Field

from .models import Profile


class CustomCheckbox(Field):
    template = 'checkbox_input.html'


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]


class UserProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = [
            'user'
        ]
