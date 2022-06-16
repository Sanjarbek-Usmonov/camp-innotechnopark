from django.urls import path
from .views import admin_index
from .category.views import *
from .project.views import *
from .person.views import *

urlpatterns = [
    path('', admin_index, name='admin'),
    path('ctg/list/', ctg_list_detail_delete, name='ctg_list'),
    path('ctg/detail/<int:pk>/', ctg_list_detail_delete, name='ctg_detail'),
    path('ctg/delete/<int:delete>/', ctg_list_detail_delete, name='ctg_delete'),
    path('ctg/add/', ctg_add_edit, name='ctg_add'),
    path('ctg/edit/<int:pk>/', ctg_add_edit, name='ctg_edit'),


    path('person/list/', person_list_detail_delete, name='person_list'),
    path('person/detail/<int:pk>/', person_list_detail_delete, name='person_detail'),
    path('person/delete/<int:delete>/', person_list_detail_delete, name='person_delete'),
    path('person/add/', person_add_edit, name='person_add'),
    path('person/edit/<int:pk>/', person_add_edit, name='person_edit'),

    path('project/list/', project_list_detail_delete, name='project_list'),
    path('project/detail/<int:pk>/', project_list_detail_delete, name='project_detail'),
    path('project/delete/<int:delete>/', project_list_detail_delete, name='project_delete'),
    path('project/add/', project_add_edit, name='project_add'),
    path('project/edit/<int:pk>/', project_add_edit, name='project_edit')
]