from django import forms
from .models import *


class LoginForm(forms.Form):
    usr = forms.CharField(label='Usuario ', max_length=25,initial="")
    pwd = forms.CharField(label='Contrasena ',widget=forms.PasswordInput(),initial="")


class LogroForm(forms.Form):
    titulo = forms.CharField(label='Titulo ', max_length=25,initial="", widget=forms.TextInput(attrs={'style': 'position: absolute; top: 17%; left: 20%; width: 20%;'}))
    detalle = forms.CharField(label='Detalle ',max_length=100,initial="", widget=forms.Textarea(attrs={'style': 'position: absolute; top: 27%; left: 10%; width: 50%; height: 20%; resize: none;'}))	