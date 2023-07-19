from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import DictionaryEntry


class AddWordForm(forms.ModelForm):
    class Meta:
        model = DictionaryEntry
        fields = ['word', 'definition', 'origin_language']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add Word'))