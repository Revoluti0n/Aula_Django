from django.db import models
from django.utils import timezone




class Contato(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

