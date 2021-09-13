from django.db import models


class Funcionario(models.Model):
    matricula = models.IntegerField('Matricula')
    nome = models.CharField(max_length=100, help_text='Nome do funcionário')
    ativo = models.BooleanField('Ativo?', default=True)

