# tasks/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, CustomUserCreationForm # Adicione esta importação
from django.contrib.auth import login # Importe a função 'login'

@login_required
def task_list(request):
    """
    Exibe a lista de tarefas e processa a criação de novas tarefas.
    """
    # Se o formulário foi submetido (método POST)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Cria a tarefa, mas não salva no banco de dados ainda
            task = form.save(commit=False)
            # Associa a tarefa ao usuário logado
            task.user = request.user
            # Salva a tarefa no banco de dados
            task.save()
            # Redireciona para a mesma página para evitar envio duplicado
            return redirect('task_list')
    else:
        # Se for uma requisição GET, cria um formulário vazio
        form = TaskForm()

    # Filtra as tarefas para mostrar apenas as do usuário atual
    tasks = Task.objects.filter(user=request.user).order_by('completed', '-id')

    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'tasks/task_list.html', context)

@login_required
def update_task(request, pk):
    """
    Inverte o status 'concluído' da tarefa.
    """
    # Encontra a tarefa ou retorna um erro 404
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    # Inverte o valor do campo 'completed'
    task.completed = not task.completed
    task.save()
    
    # Redireciona para a página inicial
    return redirect('task_list')

@login_required
def delete_task(request, pk):
    """
    Deleta uma tarefa.
    """
    # Encontra a tarefa ou retorna um erro 404
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    # Deleta a tarefa
    task.delete()
    
    # Redireciona para a página inicial
    return redirect('task_list')

def register_user(request):
    """
    Exibe e processa o formulário de registro de usuário.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Faz o login do usuário após o registro
            login(request, user)
            # Redireciona para a página inicial
            return redirect('task_list')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

from django.contrib.auth import logout # Importe a função 'logout'

def logout_user(request):
    """
    Faz o logout do usuário e o redireciona para a página de login.
    """
    logout(request)
    return redirect('login') # Redireciona para a rota 'login'