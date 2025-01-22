from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=users
        fields='__all__'
