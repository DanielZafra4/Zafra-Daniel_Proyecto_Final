from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from usuarios.models import DatosExtra
from usuarios.forms import CrearUsuarioForm, EditarPerfilForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


# Create your views here.

def login(request):
    formulario = AuthenticationForm()
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            django_login(request, usuario)
            DatosExtra.objects.get_or_create(user=usuario)
            return redirect('inicio:inicio')
    return render(request, 'usuarios/login.html',{'form': formulario})

def register(request):
    formulario = CrearUsuarioForm()
    if request.method == "POST":
        formulario = CrearUsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect('usuarios:login')
    return render(request, 'usuarios/register.html', {'form': formulario})

@login_required
def mi_perfil(request):
    datos_extra = DatosExtra.objects.get(user=request.user)
    return render(request, 'usuarios/mi_perfil.html', {'user': request.user, 'datos_extra': datos_extra})


def editar_perfil(request):
    datos_extra = request.user.datosextra 
    if request.method == 'POST':
        formulario = EditarPerfilForm(request.POST, request.FILES, instance=request.user)  # Usar la instancia de User
        if formulario.is_valid():
            formulario.save()  
            
            # Actualizar los datos extra
            datos_extra.first_name = formulario.cleaned_data.get('first_name', datos_extra.first_name)
            datos_extra.last_name = formulario.cleaned_data.get('last_name', datos_extra.last_name)
            datos_extra.gender = formulario.cleaned_data.get('gender', datos_extra.gender)
            new_avatar = formulario.cleaned_data.get('avatar')
            datos_extra.avatar = new_avatar if new_avatar else datos_extra.avatar
            
            datos_extra.save()  
            
            return redirect('usuarios:mi_perfil')  
    else:
        formulario = EditarPerfilForm(instance=request.user)  
        
    return render(request, 'usuarios/editar_perfil.html', {'form': formulario})


class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_password.html'
    success_url = reverse_lazy('usuarios:editar_perfil')