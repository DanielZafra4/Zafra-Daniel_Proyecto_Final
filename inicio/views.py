from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.models import Pokemon
from inicio.forms import crearPokemonForm, BuscarPokemonForm

def inicio(request):
    return render(request, 'inicio/index.html')


def buscar_pokemon(request):

    formulario = BuscarPokemonForm(request.GET)
    if formulario.is_valid():
        nombre = formulario.cleaned_data.get('nombre')
        tipo = formulario.cleaned_data.get('tipo')
        pokemons = Pokemon.objects.filter(nombre__icontains = nombre, tipo__icontains = tipo)
    else:    
        pokemons = Pokemon.objects.all()
    return render(request, 'inicio/buscar_pokemon.html', {'pokemons': pokemons, 'form': formulario})
    
def crear_pokemon(request):
    formulario = crearPokemonForm()
    
    if request.method == 'POST':
        
        formulario = crearPokemonForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            pokemon = Pokemon(nombre=data.get('nombre'), tipo=data.get('tipo'), nivel=data.get('nivel')) 
            pokemon.save()
            return redirect("inicio:buscar_pokemon")
    
    return render(request, 'inicio/crear_pokemon.html', {'form': formulario})

def about_me(request):
    return render(request, 'inicio/about_me.html')

    
