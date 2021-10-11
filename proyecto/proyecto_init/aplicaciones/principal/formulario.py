from django import forms
from django.db.models import fields
from .models import Persona


class formularioPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'