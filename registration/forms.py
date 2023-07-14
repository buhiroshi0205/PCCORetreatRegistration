from django import forms
from django.forms import ModelForm, modelformset_factory

from registration.models import *

class RegistrationForm(ModelForm):
  class Meta:
    model = Registration
    fields = ['small_group', 'email']
    widgets = {
      'small_group': forms.Select(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
    }

PersonFormSet = modelformset_factory(
  Person,
  fields='__all__',
  extra=4,
  widgets={
    'english_first_name': forms.TextInput(attrs={'class': 'form-control'}),
    'english_last_name': forms.TextInput(attrs={'class': 'form-control'}),
    'chinese_name': forms.TextInput(attrs={'class': 'form-control'}),
    'age': forms.NumberInput(attrs={'class': 'form-control'}),
    'status': forms.Select(attrs={'class': 'form-control'}),
    'allergies': forms.TextInput(attrs={'class': 'form-control'}),
    'dietary_restrictions': forms.TextInput(attrs={'class': 'form-control'}),
    'emergency_contact': forms.TextInput(attrs={'class': 'form-control'})
  }
)