from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.models import Pokemon
from inicio.forms import CrearPokemonForm, BuscarPokemonForm, EditarPokemonForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

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
    
def about_me(request):
    return render(request, 'inicio/about_me.html')   

class CrearPokemon(LoginRequiredMixin, CreateView):
    model = Pokemon
    form_class = CrearPokemonForm
    template_name = 'inicio/crear_pokemon.html'
    success_url = reverse_lazy('inicio:buscar_pokemon')
    
    def validar_formulario(self, form):
        return super().form_valid(form)
    

class VerPokemon(LoginRequiredMixin, DetailView):
    model = Pokemon
    template_name = "inicio/ver_pokemon.html"
    
    
class EditarPokemon(LoginRequiredMixin, UpdateView):
    model = Pokemon
    template_name = "inicio/editar_pokemon.html"
    form_class = EditarPokemonForm
    success_url = reverse_lazy('inicio:buscar_pokemon')
    
    def form_valid(self, form):
        # Si se ha marcado el checkbox para borrar la imagen, la eliminamos
        if form.cleaned_data.get('clear_imagen'):
            # Elimina la imagen del sistema de archivos
            if self.object.imagen:  # Asegúrate de que haya una imagen para eliminar
                self.object.imagen.delete(save=False)
            # Establecemos la imagen a None
            form.instance.imagen = None
        
        # Llamamos a la implementación por defecto para guardar el objeto
        return super().form_valid(form)
    

class EliminarPokemon(LoginRequiredMixin,DeleteView):
    model= Pokemon
    template_name = "inicio/eliminar_pokemon.html"
    success_url = reverse_lazy('inicio:buscar_pokemon')
    

    
