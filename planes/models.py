from django.db import models

# Create your models here.
class Plan(models.Model):
    titulo = models.CharField(max_length=50)
    velocidad = models.CharField(max_length=50)
    minutos = models.IntegerField(default=0)
    canales = models.CharField(max_length=50)
    valor = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

