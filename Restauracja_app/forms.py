from django import forms
from .models import Category, Menu, Table, Comments



class Add_MenuModelForm(forms.ModelForm):

    class Meta:
        model = Menu
        exclude = ['votes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name_input'}),
            'ingredients': forms.Textarea(attrs={'class': 'name_input'}),
            'description': forms.Textarea(attrs={'class': 'name_input'}),
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
            'description': forms.Textarea(attrs={'class': 'name_input'}),
            'slug': forms.TextInput(attrs={'class': 'name_input'})
        }
        labels = {
            'name': 'Nazwa Kategorii',
            'description': 'Opis',
            'image': 'Zdjęcie'
        }


class TableModelForm(forms.ModelForm):

    class Meta:
        model = Table
        fields = '__all__'


class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('title', 'meal', 'author', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'name_input'}),
            'text': forms.Textarea(attrs={'class': 'name_input'}),
            'author': forms.TextInput(attrs={'class': 'name_input'}),
            'meal': forms.Select(attrs={'class': 'name_input'})

        }
        labels = {
            'title': 'Tytuł',
            'text': 'Tekst',
            'author': 'Autor',
            'meal': 'Posiłek'
        }


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    email_address = forms.EmailField(max_length = 150)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Imię"
        self.fields['last_name'].label = "Nazwisko"
        self.fields['email_address'].label = "Email"
        self.fields['message'].label = "Treść"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'name_input'


