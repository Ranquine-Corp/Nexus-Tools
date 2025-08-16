# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # URL da lista de tarefas
    path('', views.task_list, name='task_list'),

    # URL para atualizar o status da tarefa
    path('update/<int:pk>/', views.update_task, name='update_task'),

    # URL para deletar uma tarefa
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]