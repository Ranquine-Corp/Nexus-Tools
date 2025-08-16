from django.db import models
from django.contrib.auth.models import User

# Documentação:
# Definimos o nosso modelo de Tarefa.
# O models.Model diz ao Django que esta classe é um modelo.
class Task(models.Model):
    # Relacionamento com o usuário.
    # Quando um usuário é deletado, todas as suas tarefas também são.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # O texto da tarefa.
    # CharField é usado para textos curtos. max_length é obrigatório.
    title = models.CharField(max_length=200)

    # Status da tarefa.
    # O valor padrão (default=False) significa que a tarefa não está concluída ao ser criada.
    completed = models.BooleanField(default=False)

    # Documentação para o retorno em string (opcional, mas boa prática).
    # Se você imprimir um objeto Task, ele retornará o título da tarefa.
    def __str__(self):
        return self.title