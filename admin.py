from django.contrib import admin
from .models import Usuario, Viatico, Notificacion, Boleta

@admin.register(Usuario)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role')
    search_fields = ('username', 'email')

@admin.register(Viatico)
class ViaticoAdmin(admin.ModelAdmin):
    list_display = ('user', 'solicitud', 'aprobado', 'created_at')
    search_fields = ('user__username', 'solicitud')

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('user', 'mensaje', 'leido', 'created_at')
    search_fields = ('user__username', 'mensaje')

@admin.register(Boleta)
class BoletaAdmin(admin.ModelAdmin):
    list_display = ('user', 'viatico', 'pdf_path', 'created_at')
    search_fields = ('user__username', 'viatico__solicitud')
