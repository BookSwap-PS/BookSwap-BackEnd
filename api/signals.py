# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from api.models.Perfil import Perfil

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     """
#     Cria automaticamente um Perfil quando um novo usuário (incluindo superusuários) é criado.
#     """
#     if created:  # Verifica se o usuário foi recém-criado
#         Perfil.objects.get_or_create(usuario=instance)
