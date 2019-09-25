from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracao = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacao = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    fotos = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)
    anexo = models.FileField(upload_to='pontos_turisticos_arquivos', null=True, blank=True)

    def __str__(self):
        return self.nome
