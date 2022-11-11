from django import forms
from .models import *


class registerform(forms.ModelForm):
    class Meta:
        model=student
        fields=('username','password','password2')
        widigets={

                  
                   'username':forms.TextInput(attrs={'class' :'form-control'}),
                   
                   'password':forms.TextInput(attrs={'class' :'form-control'}),
                   'password2':forms.TextInput(attrs={'class' :'forms-control'}),
                  

               
        }   

class registerforms(forms.ModelForm):
    class Meta:
        model=req
        fields=('name','dob','age','gender','no','email','add','subject','topic','chapter')
        widigets={

                  
                   'name':forms.TextInput(attrs={'class' :'form-control'}),
                   'dob':forms.TextInput(attrs={'class' :'form-control'}),
                   'age':forms.TextInput(attrs={'class' :'forms-control'}),
                   'gender':forms.TextInput(attrs={'class' :'form-control'}),
                   'no':forms.TextInput(attrs={'class' :'form-control'}),
                   'email':forms.TextInput(attrs={'class' :'forms-control'}),
                   'add':forms.TextInput(attrs={'class' :'forms-control'}),
                   'subject':forms.TextInput(attrs={'class' :'forms-control'}),
                   'topic':forms.TextInput(attrs={'class' :'forms-control'}),
                   'chapter':forms.TextInput(attrs={'class' :'forms-control'}),
                  

               
        }   



