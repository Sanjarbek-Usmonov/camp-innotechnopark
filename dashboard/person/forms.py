from blog.models import Person
from django import forms


class PersonForm(forms.ModelForm):
    first_name = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 32em; border-color: black'}))
    last_name = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 32em; border-color: black'}))
    address = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 32em; border-color: black'}))
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'address')


