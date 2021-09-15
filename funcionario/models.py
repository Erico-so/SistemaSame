from django.db import models
from django.contrib.auth.models import User
from unidades.models import Unidades


class Funcionario(models.Model):
    matricula = models.IntegerField('Matricula')
    nome = models.CharField(max_length=100, help_text='Nome do funcionário')
    ativo = models.BooleanField('Ativo?', default=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, unique=True)
    unid = models.ForeignKey(Unidades, on_delete=models.PROTECT)

    def __str__(self):
        return self.matricula

