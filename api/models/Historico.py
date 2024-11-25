from django.db import models
import uuid
from api.models import Livro
from django.contrib.auth.models import User


class Historico(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(User, related_name='historico_usuario', verbose_name="Usuário que solicitou", on_delete=models.PROTECT)
    usuarioDestino = models.ForeignKey(User, related_name='historico_usuarioDestino', verbose_name="Usuário alvo", on_delete=models.PROTECT)
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, verbose_name="Livro da troca")
    mensagem = models.TextField(verbose_name="Mensagem da solicitação", max_length=300)
    dataTroca = models.DateTimeField(verbose_name="Data da Troca", auto_now_add=True)
    status = models.CharField(max_length=50, verbose_name="Status da troca", default="Concluída")

    class Meta:
        verbose_name = "Histórico de Troca"
        verbose_name_plural = "Histórico de Trocas"
        ordering = ['-dataTroca']

    def __str__(self):
        return f'Troca concluída entre {self.usuario.username} e {self.usuarioDestino.username} - Livro: {self.livro.titulo}'
