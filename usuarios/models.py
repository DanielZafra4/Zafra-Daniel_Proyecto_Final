from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DatosExtra(models.Model):
    GENDER_CHOICES = [
        ('F', 'Mujer'),
        ('M', 'Hombre'),
    ]
    first_name = models.CharField(max_length=50, default='N/A')
    last_name = models.CharField(max_length=50,  default='N/A')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True)
    
    