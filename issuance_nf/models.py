from django.db import models

class Emissor(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Emissor'
        verbose_name_plural = 'Emissores'

class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    emissor = models.ForeignKey(Emissor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.numero} - {self.emissor}'

class Data(models.Model):
    data_emissao = models.DateTimeField(auto_now_add=True)
    emissor = models.ForeignKey(Emissor, on_delete=models.CASCADE) 

    @property
    def data_emissao_formatada(self):
        return self.data_emissao.strftime('%d/%m/%Y %HH:%MM')
   

    def __str__(self):
        return f'{self.data_emissao} - {self.emissor}'