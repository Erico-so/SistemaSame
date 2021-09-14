from django.db import models


class Prontuario(models.Model):
    pront = models.CharField(max_length=15, help_text='Prontuario')

    def __str__(self):
        return self.pront

