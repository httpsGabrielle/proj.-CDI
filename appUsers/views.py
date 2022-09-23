from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from appMain.models import Videos, Games, Atividades

@login_required(login_url='/accounts/login/')
def dashboard(request):
    return render(request, 'dashboard.html')
    
def escolas(request):
    return render(request, 'escolas.html')

def jogos(request):
    games = Games.objects.all()
    return render(request,'jogos-all.html',{'jogos':games})

def jogospendentes(request):
    games = Games.objects.all()
    return render(request,'jogos_pendente.html',{'jogos':games})
