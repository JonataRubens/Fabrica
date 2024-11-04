from django.shortcuts import render

def lista_alunos(request):
    # Lógica para obter os alunos e renderizar o template
    return render(request, 'index.html')