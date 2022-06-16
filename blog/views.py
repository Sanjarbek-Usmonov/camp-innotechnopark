from django.shortcuts import render
from .models import Project
# Create your views here.


def index(requests):
    query = Project.objects.all()
    return render(requests, 'index.html', {'query': query})


def about(requests, pk):
    query = Project.objects.get(pk=pk)
    return render(requests, 'about.html', {'query': query})
