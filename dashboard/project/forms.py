from blog.models import Project, Category, Person
from django import forms


class ProjectForm(forms.ModelForm):
    name = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 32em; border-color: black'}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': "form-control", 'style': 'max-width: 32em; border-color: black'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control", 'style': 'max-width: 32em; border-color: black'}))
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': "form-control", 'style': 'max-width: 32em; border-color: black'}))
    person_id = forms.ModelChoiceField(queryset=Person.objects.all(), widget=forms.Select(attrs={'class': "form-control", 'style': 'max-width: 32em; border-color: black'}))
    project_aim = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", 'style': 'max-width: 32em; border-color: black'}))
    desription = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", 'style': 'max-width: 32em; border-color: black'}))
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': "form-control", 'style': 'max-width: 32em; border-color: black'}))
    innovastion_part = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", 'style': 'max-width: 32em; border-color: black'}))
    location = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", 'style': 'max-width: 32em; border-color: black'}))

    class Meta:
        model = Project
        fields = ('name', 'image', 'price', 'category_id', 'person_id', 'project_aim', 'desription', 'file', 'innovastion_part', 'location')


