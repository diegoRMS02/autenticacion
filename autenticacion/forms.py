from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from autenticacion.models import Usuario
from .models import Viatico

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'ocupacion')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ocupacion'].required = False  # No es requerido por defecto

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        ocupacion = cleaned_data.get('ocupacion')

        # Hacer que ocupacion sea obligatorio solo si el rol es 'usuario'
        if role == 'usuario' and not ocupacion:
            self.add_error('ocupacion', 'Este campo es obligatorio para el rol de usuario.')

        return cleaned_data

class ViaticoForm(forms.ModelForm):
    class Meta:
        model = Viatico
        fields = ['solicitud', 'sustentos']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
class EditUserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'ocupacion']
