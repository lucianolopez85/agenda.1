from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    cel = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, blank=True)
    comentario = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome