from django.db import models
from django.contrib.auth.models import User
import uuid
from api.models import Livro  # Certifique-se de importar o modelo Livro

class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuarios = models.ManyToManyField(User, verbose_name="Usuários no Chat")
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="chats", null=True, blank=True)  # Relaciona com Livro
    dataCriacao = models.DateTimeField('Data de Criação', auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'
        ordering = ['dataCriacao']

    def __str__(self):
        usuarios = "-".join(list(self.usuarios.all().values_list("username", flat=True)))
        livro_titulo = self.livro.titulo if self.livro else "Sem Livro"
        return f'Conversa sobre "{livro_titulo}" entre: {usuarios}'
