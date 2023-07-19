from django import forms
from .models import DictionaryEntry
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class AddWordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add Word'))

    class Meta:
        model = DictionaryEntry
        fields = ['word', 'definition', 'origin_language']


# class AddWordForm(forms.Form):
#     word = forms.CharField(max_length=255)
#     definition = forms.CharField(widget=forms.Textarea)
#     origin_language = forms.CharField(max_length=255)
