from django.db import models


class Unidades(models.Model):
    nome = models.CharField(max_length=100, help_text='Unidade')

