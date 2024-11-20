from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student
from django.contrib.auth import password_validation

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegistrationForm(UserCreationForm):
    label1=("Password")
    label2=("Password confirmation")
    password1 = forms.CharField(
            label=label1,
            required=False,
            strip=False,
            widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class': 'form-control'}),
            help_text=password_validation.password_validators_help_text_html(),
        )
    password2 = forms.CharField(
            label=label2,
            required=False,
            widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class': 'form-control'}),
            strip=False,
            help_text=("Enter the same password as before, for verification."),
        )
    class Meta:
        model=User
        fields=['email','username','password1','password2']
        widgets={
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            }


class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widgets={
            'admission_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Admission Number'}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),
            'place':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Place'}),
            'age':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Age'}),
            'department':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Department'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter phone Number'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
            }