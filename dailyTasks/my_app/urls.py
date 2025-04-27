# my_app/views.py
# my_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('tasks/', views.index, name='task_list'),  
    path('task/<int:id>/', views.detail, name='task_detail'),  
    path('task/new/', views.create, name='task_create'),  
    path('task/<int:id>/edit/', views.edit, name='task_edit'),  
    path('task/<int:id>/delete/', views.delete, name='task_delete'),  
]


