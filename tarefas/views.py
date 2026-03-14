from django.shortcuts import render
from django.http import HttpResponse

def tarefas_home(request):
    contexto = {
        "nome": "Davi"
    }
    return render(request, 'tarefas/home.html', contexto)

def tarefas_adicionar(request):
    return HttpResponse("<h1> Adicione aqui sua tarefa!<h1>")
