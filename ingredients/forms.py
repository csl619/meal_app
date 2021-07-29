from django.forms import ModelForm, ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

from .models import Ingredient


class CustomCheckbox(Field):
    template = 'checkbox_input.html'


class NewIngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = (
            'name', 'default_unit')
        widgets = {
        }

    def __init__(self, *args, **kwargs):
        super(NewIngredientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_show_errors = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-12'
        self.helper.field_class = 'col-12'
        self.helper.layout = Layout(
            Field('name'),
            Field(
                'default_unit', css_class="selectpicker",
                data_live_search="true", data_size="5"),
        )

    def clean_name(self):
        # Get the name
        ing_name = self.cleaned_data.get('name')
        if self.instance.pk is None:
            try:
                Ingredient.objects.get(
                    name=ing_name)
            except Ingredient.DoesNotExist:
                # Unable to find the named ingredient - PASS
                return ing_name
            # An ingredient was found with this name raise an error - FAIL
            raise ValidationError(
                'There is already an ingredient with this name, please '
                'enter a different one')
        return ing_name
