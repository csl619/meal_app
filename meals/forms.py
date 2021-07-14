from django.forms import ModelForm, ValidationError, modelformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div
from crispy_forms.bootstrap import (
    AppendedText)

from .models import Meal, MealIngredient


class CustomCheckbox(Field):
    template = 'checkbox_input.html'


class NewMealForm(ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'
        exclude = ['related_user', 'last_planned', 'date_added']

    def __init__(self, *args, **kwargs):
        super(NewMealForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_show_errors = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-12'
        self.helper.field_class = 'col-12'
        self.helper.layout = Layout(
            Field('name'),
            Field(
                'related_category', css_class="selectpicker",
                data_live_search="true", data_size="5"),
            Div(
                Div(AppendedText('prep_time', 'mins'), css_class='col-sm-6'),
                Div(AppendedText('cook_time', 'mins'), css_class='col-sm-6'),
                css_class='row'
            ),
            Field('recipe', css_class='tinymce'),
            Field('notes', css_class='tinymce-sm'),

        )

    def clean_name(self):
        # Get the name
        meal_name = self.cleaned_data.get('name')
        if self.instance.pk is None:
            try:
                Meal.objects.get(
                    name=meal_name)
            except Meal.DoesNotExist:
                # Unable to find the named ingredient - PASS
                return meal_name
            # An ingredient was found with this name raise an error - FAIL
            raise ValidationError(
                'There is already a meal with this name, please '
                'enter a different one')
        return meal_name


class IngredientLine(ModelForm):
    class Meta:
        model = MealIngredient
        fields = (
            'related_ingredient', 'amount', 'unit')
        widgets = {
        }
        exclude = [
            ''
            ]

    def __init__(self, *args, **kwargs):
        super(IngredientLine, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_show_errors = True
        self.helper.form_show_labels = False
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap4/layout/inline_field.html'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(Field(
                        'related_ingredient', css_class="selectpicker",
                        data_live_search="true", data_size="5"),
                        css_class="col-sm-4"),
                    Div(Field('amount'), css_class="col-sm-4"),
                    Div(Field(
                        'unit', css_class="selectpicker",
                        data_live_search="true", data_size="5"),
                        css_class="col-sm-4"),
                    Div(
                        Field('DELETE', css_class='d-none'),
                        css_class="d-none"),
                    css_class='row',
                ),
                css_class='col-md-11'
            ),

        )

ingredient_formset = modelformset_factory(
    MealIngredient,
    form=IngredientLine,
    extra=1,
    can_delete=True
)