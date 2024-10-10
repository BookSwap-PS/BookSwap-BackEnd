# Importa todos os serializers relevantes para o sistema, incluindo os necessários para perfis
from .LivroSerializer import LivroSerializer
from .UserSerializer import UserSerializer
from .PerfilSerializer import PerfilSerializer, PerfilCreateUpdateSerializer, PerfilSearchSerializer  # Adiciona o PerfilSearchSerializer para busca de perfis