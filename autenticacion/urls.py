from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('registrar_viatico/', views.registrar_viatico, name='registrar_viatico'),
    path('home/', views.home, name='home'), 
    path('login/', views.login_view, name='login'),
    path('listar_viaticos/', views.listar_viaticos, name='listar_viaticos'),
    path('aprobar_viatico/<int:viatico_id>/', views.aprobar_viatico, name='aprobar_viatico'),
    path('logout/', views.logout_view, name='logout'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('editar_usuario/<int:user_id>/', views.editar_usuario, name='editar_usuario'),
    path('historial_viaticos/', views.historial_viaticos, name='historial_viaticos'),
    path('almacen/', views.almacen, name='almacen'),
]
