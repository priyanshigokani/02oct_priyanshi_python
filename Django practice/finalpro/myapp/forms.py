from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'

class updForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields=['firstname','lastname','username','password','city','state','mobile']

class NotesForm(forms.ModelForm):
    class Meta:
        model=notes
        fields=['username','title','opt','myfile','desc']

class contactForm(forms.ModelForm):
    class Meta:
        model = contactus
        fields = "__all__"