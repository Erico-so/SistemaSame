from django.db import models
from django.contrib.auth.models import User


class Unidades(models.Model):
    nome = models.CharField(max_length=100, help_text='Unidade')
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.nome

