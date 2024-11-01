from django.db import models
from datetime import date

# Create your models here.
class Pokemon(models.Model):
   nombre = models.CharField(max_length=20)
   tipo = models.CharField(max_length=50)
   nivel = models.IntegerField()
   imagen = models.ImageField(upload_to='pokemon_imagenes/', blank=True, null=True)
   fecha = models.DateField(default=date.today)

   
   def __str__(self):
        return f'ID: {self.id} | Nombre: {self.nombre} | Tipo: {self.tipo}'
