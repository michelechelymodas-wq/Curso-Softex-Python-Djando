
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer
from rest_framework import status

class ListaTarefasAPIView(APIView):
    def post(self, request, format=None):
        """
            Cria uma nova tarefa.

            Args:
                request.data: JSON com dados da tarefa
            {
            "titulo": "string",
            "concluida": boolean (opcional, default=False)
            }

            Returns:
            201 Created: Tarefa criada com sucesso
            400 Bad Request: Dados inválidos
        """
 # 1. INSTANCIAR: Criar serializer com dados recebidos
        serializer = TarefaSerializer(data=request.data)

 # 2. VALIDAR: Checar se os dados são válidos
    
 # 3. SALVAR: Persistir no banco de dados
    

 # 4. RESPONDER: Retornar objeto criado + status 201
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
 )

 # 5. ERRO: Retornar erros de validação + status 400
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
)       
    
class ListaTarefasAPIView(APIView):
       
    def get(self, request, format=None):
    
   
        tarefas = Tarefa.objects.all()
        
        serializer = TarefaSerializer(tarefas, many=True)
    

class EstatisticasTarefas(APIView):
    def get(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(status='concluida').count()
        pendentes = total - concluidas
        taxa_conclusao = concluidas / total if total > 0 else 0
        
        return Response({
            "total": total,
            "concluidas": concluidas,
            "pendentes": pendentes,
            "taxa_conclusao": taxa_conclusao
        }, status=status.HTTP_200_OK)