from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from inicio import views
from inicio.views import (
    inicio,
    buscar_pokemon,
    about_me
)

app_name = "inicio"

urlpatterns = [
    path('', inicio, name="inicio"),
    path('pokemon/', buscar_pokemon, name="buscar_pokemon"),
    path('pokemon/crear/', views.CrearPokemon.as_view(), name="crear_pokemon"),
    path('about-me/', about_me, name="about_me"),
    path('pokemon/<int:pk>/', views.VerPokemon.as_view(), name = 'ver_pokemon' ),
    path('pokemon/<int:pk>/editar', views.EditarPokemon.as_view(), name='editar_pokemon'),
    path('pokemon/<int:pk>/eliminar', views.EliminarPokemon.as_view(), name = 'eliminar_pokemon' )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
