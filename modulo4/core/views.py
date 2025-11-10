from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarefa
from .models import Execucao
   

# Create your views here.
def home(request):
    todas_as_tarefas = Tarefa.objects.all()
    todas_as_tarefas = Execucao.objects.all()
    #return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")
    context = { 
        'nome_usuario': 'Júnior', 
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS'],
        "tarefas": todas_as_tarefas,
        "execucoes": todas_as_tarefas,
    }

    return render(request, 'home.html', context)


#def inicio(request):
    return HttpResponse("<h1>Olá, Mundo! Esta é minha segunda página Django, que alegria!</h1>")

   