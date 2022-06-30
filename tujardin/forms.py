from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Tipo, Producto, cliente


class prodform(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['idprod', 'nomprod', 'precio', 'tipo','imgpro']
        labels ={
            'idprod': 'idprod', 
            'nomprod': 'nomprod', 
            'precio': 'precio', 
            'tipo': 'tipo',
            'imgpro': 'imgpro',
        }
        widgets={
            'idprod': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Id', 
                    'id': 'idprod'
                }
            ), 
            'imgpro': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese imagen', 
                    'id': 'imgpro'
                }
            ),
            'nomprod': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre', 
                    'id': 'nomprod'
                }
            ), 
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Precio', 
                    'id': 'precio'
                }
            ), 
            'tipo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tipo',
                }
            )

        }

class clientform(forms.ModelForm):

    class Meta: 
        model= cliente
        fields = [ 'nom', 'email', 'idcli']
        labels ={
            'nom': 'nom', 
            'email': 'email', 
            'idcli': 'idcli',
        }
        widgets={
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Gmail', 
                    'id': 'email'
                }
            ), 
            'nom': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre', 
                    'id': 'nom'
                }
            ), 
            'idcli': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese ID Cliente', 
                    'id': 'idcli'
                }
            ), 
        }