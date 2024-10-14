from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, ViaticoForm, CustomAuthenticationForm
from .models import Viatico

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
        form = ViaticoForm(request.POST)
        if form.is_valid():
            viatico = form.save(commit=False)
            viatico.user = request.user
            viatico.save()
            return redirect('home')
    else:
        form = ViaticoForm()
    return render(request, 'registrar_viatico.html', {'form': form})
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
