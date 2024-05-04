from django.db import models
from base.models import Usuario

# Create your models here.
class Conta(models.Model):
    nome_conta = models.CharField("Nome da conta", max_length=200)
    descricao_conta = models.TextField("Descrição da conta")
    # adicionar choices moeda
    class Meta:
        verbose_name = "Conta"
        verbose_name_plural = "Contas"

    def __str__(self):
        return self.nome_conta

class ContaUsuario(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    saldo = models.DecimalField("Saldo", decimal_places=2, max_digits=14, default=0)

    class Meta:
        verbose_name = "ContaCliente"
        verbose_name_plural = "ContasClientes"

    def __str__(self):
        return f"{self.usuario} - {self.conta}"