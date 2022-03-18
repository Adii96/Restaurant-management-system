from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import linebreaks

from .models import Category, Menu
from django.utils.safestring import mark_safe


class Add_MenuModelForm(forms.ModelForm):

    class Meta:
        model = Menu
        exclude = ['votes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name_input'}),
            'ingredients': forms.TextInput(attrs={'class': 'name_input'}),
            'description': forms.TextInput(attrs={'class': 'name_input'}),
            'price': forms.NumberInput(attrs={'class': 'name_input'}),
            'votes': forms.NumberInput(attrs={'class': 'name_input'}),
            'category': forms.Select(attrs={'class': 'name_input'}),

        }
        labels = {
            'name': 'Nazwa Dania',
            'ingredients': 'Składniki',
            'description': 'Opis',
            'price': 'Cena',
            'votes': 'Ocena',
            'category': 'Kategoria',
            'image': 'Zdjęcie'
        }

class Add_CategoryModelForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name_input'}),
            'description': forms.TextInput(attrs={'class': 'name_input'}),
            'slug': forms.TextInput(attrs={'class': 'name_input'})
        }
        labels = {
            'name': 'Nazwa Kategorii',
            'description': 'Opis',
            'image': 'Zdjęcie'
        }

