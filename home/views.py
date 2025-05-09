
from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .models import Produto # não estava importando o modelo produto

def cadastrar_produto(request):
    form = ProdutoForm(request.POST or None) # Corrigido para aceitar quando não for POST
    if form.is_valid():
        form.save()
        return redirect('listar_produto')  # Após salvar, redireciona para a listagem
    return render(request, 'home/cadastro.html', {'form': form}) # Corrigido o caminho do template

def listar_produto(request):
    produtos = Produto.objects.all() # modelo 'Produto' com 'P' maiúsculo
    return render(request, 'home/listar.html', {'produtos': produtos}) # Corrigido o caminho do template