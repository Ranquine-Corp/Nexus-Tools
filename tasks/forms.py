# tasks/forms.py

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    """
    Formulário para criar e editar tarefas,
    baseado no nosso modelo Task.
    """
    class Meta:
        # Associa o formulário ao modelo Task
        model = Task
        # Define os campos que estarão no formulário
        fields = ['title']