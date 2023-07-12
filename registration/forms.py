from django import forms
from django.forms import ModelForm, modelformset_factory

from registration.models import *

class RegistrationForm(ModelForm):
  class Meta:
    model = Person
    fields = '__all__'

PersonFormSet = modelformset_factory(Person, fields='__all__')