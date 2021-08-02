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
        exclude = ['user', 'food_order_day', 'meal_repeat', 'profile_setup']

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


class NewProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = [
            'user', 'profile_setup',
        ]

    def __init__(self, *args, **kwargs):
        super(NewProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_show_errors = True
        self.helper.form_show_labels = True
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap4/layout/inline_field.html'
        self.helper.layout = Layout(
            Field('food_order_day'),
            AppendedText('meal_repeat', 'days', min=7, max=28),
            Field(
                'monday', css_class="selectpicker",
                data_live_search="true", data_size="5"),
            Field(
                'tuesday', css_class="selectpicker",
                data_live_search="true", data_size="5"),
            Field(
                'wednesday', css_class="selectpicker",
                data_live_search="true", data_size="5"),
            Field(
                'thursday', css_class="selectpicker",
                data_live_search="true", data_size="5"),
            Field(
                'friday', css_class="selectpicker",
                data_live_search="true", data_size="5"),
            Field(
                'saturday', css_class="selectpicker",
                data_live_search="true", data_size="5"),
            Field(
                'sunday', css_class="selectpicker",
                data_live_search="true", data_size="5"),

        )
