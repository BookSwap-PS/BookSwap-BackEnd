from rest_framework import serializers
from api.models import Historico
from api.serializers import LivroSerializer, UserSerializer

class HistoricoSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    usuarioDestino = UserSerializer(read_only=True)
    livro = LivroSerializer(read_only=True)

    class Meta:
        model = Historico
        fields = '__all__'
