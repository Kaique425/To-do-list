from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarefas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(null=True, blank=True)
    completa = models.BooleanField(default=False)
    data_de_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['completa']
