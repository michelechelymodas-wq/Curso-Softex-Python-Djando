from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarefa
from .models import Execucao
from .forms import TarefaForm


   

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
# 5. Salva o objeto no banco de dados!
            form.save()
# 6. Redireciona de volta para a 'home'
# Isso é o Padrão "Post-Redirect-Get" (PRG)
            return redirect('home')
# Se o form NÃO for válido, o código continua e
# o 'form' (com os erros) será enviado para o template
# 7. Lógica de GET: Se o usuário apenas visitou a página
    else:
        form = TarefaForm() # Cria um formulário vazio
# 8. A busca de dados (fora dos 'ifs', pois é necessária sempre)
    todas_as_tarefas = Tarefa.objects.all().order_by('-criada_em') # Ordena pelas mais novas
# 9. Atualize o contexto para incluir o formulário
    context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'Models', 'Forms'],
        'tarefas': todas_as_tarefas,
        'form': form, # 10. Envie o 'form' (vazio ou com erros) para o template
    }
    return render(request, 'home.html', context)


    todas_as_tarefas = Tarefa.objects.all()
    
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

   