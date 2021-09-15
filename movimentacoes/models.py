from django.db import models
from prontuarios.models import Prontuario
from status.models import Status
from funcionario.models import Funcionario


class Movimentacao(models.Model):
    num_pront = models.ManyToManyField(Prontuario)
    data_mov = models.DateField()
    st = models.ManyToManyField(Status)
    usu = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.num_pront
