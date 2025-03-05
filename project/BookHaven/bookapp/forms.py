from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=signup
        fields="__all__"
        
class adddbookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['auname', 'booktitle', 'pdate', 'description', 'genre', 'img', 'myfile']
        widgets = {
            'genre': forms.CheckboxSelectMultiple(),  # This will render the genres as checkboxes
        }

class au_ap(forms.ModelForm):
    class Meta:
        model=Author
        fields=['user','email','number','bio']