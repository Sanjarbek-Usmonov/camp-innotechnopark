from django.urls import path
# from .category.views import CategoryView, CategoryListView
from .category.views import CategoryView, CategoryListView
from .person.views import *
from .project.views import *

urlpatterns = [
    path('category/<int:pk>/', CategoryView.as_view(), name='api_ctg_one'),
    path('category/', CategoryListView.as_view(), name='api_ctg_list'),

    path('person/<int:pk>/', PersonView.as_view(), name='api_person_one'),
    path('person/', PersonListView.as_view(), name='api_person_list'),

    path('project/<int:pk>/', ProjectView.as_view(), name='api_project_one'),
    path('project/', ProjectListView.as_view(), name='api_project_list'),
]

