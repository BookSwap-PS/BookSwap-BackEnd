# Generated by Django 5.1 on 2024-09-16 13:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_livro_condicao_livro_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='atualizado_em',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='livro',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]