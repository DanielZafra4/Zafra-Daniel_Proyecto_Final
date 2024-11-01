from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import DatosExtra

class CrearUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
        
class EditarPerfilForm(UserChangeForm):
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    gender = forms.ChoiceField(label='Género', choices=DatosExtra.GENDER_CHOICES) # Cambiado a ChoiceField
    email = forms.EmailField(label='Correo electrónico')
    password = None
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender', 'email','avatar']