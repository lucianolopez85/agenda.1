from django.shortcuts import render


def metodo_index(request):
    return render(request, 'contatos/index.html')