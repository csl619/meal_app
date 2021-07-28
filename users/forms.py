from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.layout import Layout, Field
from crispy_forms.bootstrap import (AppendedText)
from crispy_forms.helper import FormHelper

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


class MealCatForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'food_order_day', 'meal_repeat']

    def __init__(self, *args, **kwargs):
        super(MealCatForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_show_errors = True
        self.helper.form_class = 'form-horizontal row'
        self.helper.label_class = 'col-6 col-md-5'
        self.helper.field_class = 'col-6 col-md-7'


class MealRepeatForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'meal_repeat',
        ]

    def __init__(self, *args, **kwargs):
        super(MealRepeatForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_show_errors = True
        self.helper.form_class = 'form-horizontal row'
        self.helper.label_class = 'col-6 col-md-5'
        self.helper.field_class = 'col-6 col-md-7'
        self.helper.layout = Layout(
            AppendedText('meal_repeat', 'days', min=7, max=28),

        )
