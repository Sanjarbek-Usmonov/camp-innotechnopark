from django.contrib import admin
from .models import Project, Person, Category
# Register your models here.

admin.site.register(Project)
admin.site.register(Person)
admin.site.register(Category)

