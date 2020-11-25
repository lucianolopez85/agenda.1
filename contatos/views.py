from django.shortcuts import render
from .models import Contato


def metodo_index(request):
    contato = Contato.objects.all()
    return render(request, 'contatos/index.html', 
    {
        'key_contato': contato
    })


def metodo_detalhe(request, contato_detalhe_id):
    contato_detalhe = Contato.objects.get(id=contato_detalhe_id)
    return render(request, 'contatos/detalhe.html', 
    {
        'key_contato_detalhe': contato_detalhe
    })