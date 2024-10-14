from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('registrar_viatico/', views.registrar_viatico, name='registrar_viatico'),
    path('home/', views.home, name='home'), 
    path('login/', views.login_view, name='login')

]
