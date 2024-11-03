# Generated by Django 5.1 on 2024-11-03 18:08

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_comentario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Criação')),
                ('usuarios', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Usuários no Chat')),
            ],
            options={
                'verbose_name': 'Chat',
                'verbose_name_plural': 'Chats',
                'ordering': ['dataCriacao'],
            },
        ),
        migrations.CreateModel(
            name='ChatMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField(default=' ', max_length=2800, verbose_name='Conteúdo da Mensagem')),
                ('dataEnvio', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Envio')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.chat', verbose_name='Chat')),
                ('quemEnviou', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quemEnviou', to=settings.AUTH_USER_MODEL, verbose_name='Quem enviou')),
                ('quemLeu', models.ManyToManyField(related_name='quemLeu', to=settings.AUTH_USER_MODEL, verbose_name='Usuários que leram')),
                ('quemRecebeu', models.ManyToManyField(related_name='quemRecebeu', to=settings.AUTH_USER_MODEL, verbose_name='Usuários que receberam')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ['chat', 'dataEnvio'],
            },
        ),
        migrations.CreateModel(
            name='ChatRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mensagem', models.TextField(default=' ', max_length=300, verbose_name='Conteúdo da Mensagem de solicitação')),
                ('aceito', models.BooleanField(default=False, verbose_name='Aceitou a solicitação?')),
                ('dataCriacao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Criação')),
                ('chat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.chat', verbose_name='Chat')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuario_solicitante', to=settings.AUTH_USER_MODEL, verbose_name='Usuário que solicitou o Chat')),
                ('usuarioDestino', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuario_alvo', to=settings.AUTH_USER_MODEL, verbose_name='Usuário alvo do Chat')),
            ],
            options={
                'verbose_name': 'Solicitação de Chat',
                'verbose_name_plural': 'Solicitações de Chats',
                'ordering': ['dataCriacao'],
            },
        ),
    ]
