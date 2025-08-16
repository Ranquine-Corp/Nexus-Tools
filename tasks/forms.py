# tasks/forms.py

from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm # Adicione esta linha!

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

class CustomUserCreationForm(UserCreationForm):
    """
    Formulário de criação de usuário personalizado.
    """
    class Meta(UserCreationForm.Meta):
        # Usa o modelo de usuário padrão do Django
        model = UserCreationForm.Meta.model
        # Define os campos que estarão no formulário
        fields = UserCreationForm.Meta.fields + ('email',)