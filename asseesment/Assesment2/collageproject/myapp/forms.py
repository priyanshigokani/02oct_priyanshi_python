from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'    


class addTeaForm(forms.ModelForm):
    class Meta:
        model=addTea
        fields='__all__'

class addStuForm(forms.ModelForm):
    class Meta:
        model=addStu
        fields='__all__'

class aBooks(forms.ModelForm):
    class Meta:
        model=addB
        fields='__all__'

class aEve(forms.ModelForm):
    class Meta:
        model=addEve
        fields='__all__'

class updData(forms.ModelForm):
    class Meta:
        model=signup
        fields=['id','username','email','password']
 
class eve(forms.ModelForm):
    class Meta:
        model=addEve
        fields=['EventTitle','date','img','desc']


class pas(forms.ModelForm):
    class Meta:
        model = signup
        fields = ['password']
