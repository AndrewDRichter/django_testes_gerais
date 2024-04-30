from django.db import models

# Create your models here.
class Conta(models.Model):
    nome_conta = models.CharField("Nome da conta", max_length=200)
    descricao_conta = models.TextField("Descrição da conta")
    # adicionar choices moeda
    class Meta:
        verbose_name = "Conta"
        verbose_name_plural = "Contas"

class ContaCliente(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)
    cliente = models.CharField("Cliente", max_length=200)