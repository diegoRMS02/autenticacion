from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout, get_user_model
from .forms import CustomUserCreationForm, ViaticoForm, CustomAuthenticationForm
from .models import Viatico
from .forms import EditUserForm
User = get_user_model()
@login_required
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def registrar_viatico(request):
    if request.method == 'POST':
        solicitud = request.POST['solicitud']
        sustentos = request.POST['sustentos']
        viatico = Viatico(user=request.user, solicitud=solicitud, sustentos=sustentos)
        viatico.save()
        return redirect('home')
    return render(request, 'registrar_viatico.html')

@login_required
def listar_viaticos(request):
    if request.user.role not in ['administrador', 'gerencia']:
        return redirect('home')
    viaticos = Viatico.objects.all()
    return render(request, 'listar_viaticos.html', {'viaticos': viaticos})

@login_required
def ver_viatico(request, viatico_id):
    if request.user.role not in ['administrador', 'gerencia']:
        return redirect('home')
    viatico = Viatico.objects.get(id=viatico_id)
    if request.method == 'POST':
        viatico.aprobado = True
        viatico.save()
        return redirect('listar_viaticos')
    return render(request, 'aprobar_viatico.html', {'viatico': viatico})

from django.shortcuts import render
@login_required
def home(request):
    return render(request, 'index.html')



def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})
@login_required
def aprobar_viatico(request, viatico_id):
    if request.user.role not in ['administrador', 'gerencia']:
        return redirect('home')
    viatico = Viatico.objects.get(id=viatico_id)
    if request.method == 'POST':
        viatico.aprobado = True
        viatico.save()
        return redirect('listar_viaticos')
    return render(request, 'aprobar_viatico.html', {'viatico': viatico})
def logout_view(request):
    logout(request)
    return redirect('login')

def listar_usuarios(request): 
    usuarios = User.objects.all() 
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})
def editar_usuario(request, user_id): 
    usuario = get_object_or_404(User, id=user_id) 
    if request.method == 'POST': 
        form = EditUserForm(request.POST, instance=usuario) 
        if form.is_valid(): form.save() 
        return redirect('listar_usuarios') 
    else: 
        form = EditUserForm(instance=usuario) 
    return render(request, 'editar_usuario.html', {'form': form})