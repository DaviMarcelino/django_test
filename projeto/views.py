from django.http import HttpResponse

def index_view(request):
    return HttpResponse("<h1>Bem Vindo!</h1>")

def teste_view(request):
    return HttpResponse("<h1>Essa é a rota de teste!</h1>")