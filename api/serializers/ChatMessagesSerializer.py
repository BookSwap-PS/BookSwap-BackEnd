from rest_framework import serializers
from api.models import ChatMessages, Chat

class ChatMessagesSerializer(serializers.ModelSerializer):
    quemEnviou = serializers.CharField(source='quemEnviou.username')  # Exibe o username de quem enviou
    quemRecebeu = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'  # Exibe os usernames de quem recebeu
    )
    quemLeu = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'  # Exibe os usernames de quem leu
    )
    tituloTroca = serializers.SerializerMethodField()  # Campo personalizado para "Troca - nome do livro"
    usuariosEnvolvidos = serializers.SerializerMethodField()  # Lista de usuários no chat

    class Meta:
        model = ChatMessages
        fields = ['id', 'conteudo', 'quemEnviou', 'quemRecebeu', 'quemLeu', 'dataEnvio', 'tituloTroca', 'usuariosEnvolvidos']

    def get_tituloTroca(self, obj):
        # Obtém o livro associado ao chat e retorna "Troca - Nome do Livro"
        chat = obj.chat
        livro = chat.livro if hasattr(chat, 'livro') else None
        return f"Troca - {livro.titulo}" if livro else "Troca - Sem Título"

    def get_usuariosEnvolvidos(self, obj):
        # Obtém os usuários envolvidos no chat
        return [usuario.username for usuario in obj.chat.usuarios.all()]
