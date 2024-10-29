# Generated by Django 5.1 on 2024-10-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_perfil_criado_em'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='seguidores',
            field=models.ManyToManyField(blank=True, related_name='Seguidores', to='api.perfil'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='seguindo',
            field=models.ManyToManyField(blank=True, related_name='Seguindo', to='api.perfil'),
        ),
    ]
