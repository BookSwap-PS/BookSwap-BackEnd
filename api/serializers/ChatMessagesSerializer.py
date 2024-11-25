from rest_framework import serializers
from api.models import ChatMessages

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

    class Meta:
        model = ChatMessages
        fields = ['id', 'conteudo', 'quemEnviou', 'quemRecebeu', 'quemLeu', 'dataEnvio']
