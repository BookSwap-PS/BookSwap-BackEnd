from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.models import Chat, ChatMessages
from api.serializers import ChatSerializer, ChatMessagesSerializer

class GetUserChatMessages(viewsets.ViewSet, APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        Retorna os chats do usuário com mensagens associadas.
        """
        chats = Chat.objects.filter(usuarios=request.user)
        serialized_chats = ChatSerializer(chats, many=True).data
        return Response(serialized_chats, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Retorna as mensagens de um chat específico.
        """
        chat_id = kwargs.get('pk')
        try:
            chat = Chat.objects.get(id=chat_id, usuarios=request.user)
        except Chat.DoesNotExist:
            return Response({'erro': 'Chat não encontrado ou você não tem acesso a ele.'}, 
                            status=status.HTTP_404_NOT_FOUND)

        serialized_chat = ChatSerializer(chat).data
        return Response(serialized_chat, status=status.HTTP_200_OK)
    def create(self, request, *args, **kwargs):
        # Método de criação de mensagens não permitido nesta view
        return Response({'mensagem': 'Não permitido!'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        # Método de destruição não permitido nesta view
        return Response({'mensagem': 'Não permitido!'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
