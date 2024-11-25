from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.models import Historico
from api.serializers import HistoricoSerializer
from django.db.models import Q

class HistoricoTrocasView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user')
        if user_id:
            # Busca por histórico onde o usuário é solicitante ou destinatário
            historico = Historico.objects.filter(
                Q(usuario_id=user_id) | Q(usuarioDestino_id=user_id)
            ).order_by('-dataTroca')
        else:
            historico = Historico.objects.all().order_by('-dataTroca')

        # Passando o contexto para o serializer
        serializer = HistoricoSerializer(historico, many=True, context={'request': request})
        return Response(serializer.data)
