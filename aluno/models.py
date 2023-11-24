from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=40)
    email = models.EmailField(max_length=80)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Quarto(models.Model):
    apartamento = models.IntegerField()
    valor = models.FloatField()

    def __str__(self):
        return f"{self.apartamento}"


class Hospedagem(models.Model):
    data_entrada = models.DateField()
    data_saida = models.DateField()
    valor = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)


class Consumo(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    valor = models.FloatField()
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)
