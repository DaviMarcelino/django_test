from django.shortcuts import render
from django.http import HttpResponse

def tarefas_home(request):
    return HttpResponse("<h1>aqui estão suas tarefas:<h1>")

def tarefas_adicionar(request):
    return HttpResponse("<h1> Adicione aqui sua tarefa!<h1>")
