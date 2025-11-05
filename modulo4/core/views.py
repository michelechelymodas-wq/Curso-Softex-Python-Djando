from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")
    context = { 
        'nome_usuario': 'Júnior', 
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS']
    }

    return render(request, 'home.html', context)


#def inicio(request):
    return HttpResponse("<h1>Olá, Mundo! Esta é minha segunda página Django, que alegria!</h1>")
   