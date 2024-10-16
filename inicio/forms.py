from django import forms 

class crearPokemonForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=50)
    nivel = forms.IntegerField()
    
class BuscarPokemonForm(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    tipo =  forms.CharField(max_length=50, required=False)