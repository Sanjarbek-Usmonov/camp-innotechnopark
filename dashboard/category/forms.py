from blog.models import Category
from django import forms


class CtgForm(forms.ModelForm):
    name = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 32em; border-color: black'}))
    class Meta:
        model = Category
        fields = ('name',)


