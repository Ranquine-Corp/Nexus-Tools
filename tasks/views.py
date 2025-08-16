from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
    def task_list(request):
        """
    Exibe a lista de tarefas do usuário logado.
    """
     # Filtra as tarefas para mostrar apenas as do usuário atual
     tasks = Task.objects.filter(user=request.user).order_by('completed', '-id')
     
    # Passa as tarefas para o template (a página HTML)
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/task_list.html', context)