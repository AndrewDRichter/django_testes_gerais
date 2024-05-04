from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    data_cad = models.DateTimeField("Data de cadastro", auto_created=True)
    data_ult_alt = models.DateTimeField("Ultima alteracao", auto_now=True)
    ativo = models.BooleanField(default=True)

class Usuario(User):
    contato = models.CharField("Contato", max_length=200)
    endereco = models.CharField("Endereço", max_length=200)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.username