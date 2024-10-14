from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLE_CHOICES = (
        ('usuario', 'Usuario'),
        ('administrador', 'Administrador'),
        ('gerencia', 'Gerencia'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

class Viatico(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    solicitud = models.TextField()
    sustentos = models.TextField()
    aprobado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Asegúrate de que esta línea esté presente
    updated_at = models.DateTimeField(auto_now=True)      # Asegúrate de que esta línea esté presente

class Notificacion(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje = models.TextField()
    leido = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Boleta(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    viatico = models.ForeignKey(Viatico, on_delete=models.CASCADE)
    pdf_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
