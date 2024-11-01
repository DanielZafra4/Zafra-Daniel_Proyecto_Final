from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('perfil/', views.mi_perfil, name="mi_perfil"),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/editar/password', views.CambiarPassword.as_view(), name='cambiar_password')
]