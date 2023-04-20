from django import forms
from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'parent', 'explicit_url',]

    def clean_explicit_url(self):
        return self.cleaned_data['explicit_url'] or None
