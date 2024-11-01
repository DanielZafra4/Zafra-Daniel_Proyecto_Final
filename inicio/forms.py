from django import forms 
from .models import Pokemon

class CrearPokemonForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre del Pokémon', max_length=20)
    tipo = forms.CharField(label='Tipo', max_length=50)
    nivel = forms.IntegerField(label='Nivel')
    imagen = forms.ImageField(label='Imagen del Pokémon', required=False)
    fecha = forms.DateField(label='Fecha de Captura')
    
    class Meta:
        model = Pokemon
        fields = ['nombre', 'tipo', 'nivel', 'imagen', 'fecha']
    
class BuscarPokemonForm(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    tipo =  forms.CharField(max_length=50, required=False)
    
class EditarPokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['nombre', 'tipo', 'nivel', 'imagen', 'fecha']