# Generated by Django 5.1 on 2024-11-25 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_historico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='pontuacao',
            field=models.IntegerField(default=1),
        ),
    ]
