from django import forms
from .models import Tarefa 
from projects.models import Project # Importe o Project

# Importe o Model
# Esta classe herda de 'ModelForm'
class TarefaForm(forms.ModelForm):
     def __init__(self, *args, **kwargs):
         user = kwargs.pop('user', None)
         super(TarefaForm, self).__init__(*args, **kwargs)  
         if user:
            self.fields['project'].queryset = Project.objects.filter(user=user)

# A "mágica" acontece aqui, na classe 'Meta'
     class Meta:
    # 1. Diga ao form qual Model ele deve usar
        model = Tarefa
    # 2. Diga quais campos do Model devem virar campos no form
    # Nós só queremos que o usuário defina o 'titulo'.
    # 'concluida' (default=False) e 'criada_em' (auto_now_add=True)
    # serão preenchidos automaticamente pelo Model.
        fields = ['titulo','project' ]
