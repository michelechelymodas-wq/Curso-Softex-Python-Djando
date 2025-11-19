from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from .forms import TarefaForm

@login_required
def home(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            tarefa = form.save(commit=False) 
            # Atribui o usuário logado (request.user) ao campo 'user' da tarefa 
            tarefa.user = request.user 

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
    todas_as_tarefas = Tarefa.objects.filter(user=request.user).all().order_by('-criada_em') # Ordena pelas mais novas
# 9. Atualize o contexto para incluir o formulário
    context = {
        'nome_usuario': 'Michele',
        'tecnologias': ['Python', 'Django', 'Html', 'Css'],
        'tarefas': todas_as_tarefas,
        'form': form, # 10. Envie o 'form' (vazio ou com erros) para o template
    }
    return render(request, 'home.html', context)


    todas_as_tarefas = Tarefa.objects.all()
    
    #return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")
    context = { 
        'nome_usuario': 'Michele', 
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS'],
        "tarefas": todas_as_tarefas,
        "execucoes": todas_as_tarefas,
    }

    return render(request, 'home.html', context)


#def inicio(request):
    return HttpResponse("<h1>Olá, Mundo! Esta é minha segunda página Django, que alegria!</h1>")
@login_required
def concluir_tarefa(request, pk):     

    # 1. Busca a tarefa pela 'pk' (ID) vinda da URL.      
    # Se não achar, retorna um erro 404.     
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)   

    # 2. Segurança: Apenas execute se o método for POST     
    if request.method == 'POST':         
        # 3. A Lógica de "Update"         
        tarefa.concluida = True         
        tarefa.save() # Não se esqueça de salvar!                  
    
        # 4. Redireciona de volta para a 'home' (Padrão PRG)         
        return redirect('home')  

@login_required
def deletar_tarefa(request, pk):     
    # 1. Busca a tarefa     
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)     

    # 2. Segurança: Apenas execute se o método for POST     
    if request.method == 'POST':      
        # 3. A Lógica de "Delete"        
        tarefa.delete()          
 
        # 4. Redireciona de volta para a 'home'         
        return redirect('home')
    
def register(request): 
    # Se a requisição for POST, o usuário enviou o formulário 
     if request.method == 'POST': 

        # Cria uma instância do formulário com os dados enviados 
        form = UserCreationForm(request.POST) 

        # Verifica se o formulário é válido (ex: senhas batem, username não existe) 
        if form.is_valid(): 
            user = form.save() # Salva o novo usuário no banco 
            login(request, user) # Faz o login automático do usuário 
            return redirect('home') # Redireciona para a home 
        
    # Se a requisição for GET, o usuário apenas visitou a página 
     else: 
        form = UserCreationForm() # Cria um formulário de cadastro vazio 
     
    # Prepara o contexto e renderiza o template 
     context = {'form': form} 
     return render(request, 'register.html', context)