from django.db import models

# Create your models here.
class Pokemon(models.Model):
   nombre = models.CharField(max_length=20)
   tipo = models.CharField(max_length=50)
   nivel = models.IntegerField()

   
   def __str__(self):
        return f'ID: {self.id} | Nombre: {self.nombre} | Tipo: {self.tipo}'
