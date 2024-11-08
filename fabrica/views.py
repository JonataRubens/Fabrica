from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from fabrica.forms import  CursoForm, AlunoForm, CampusForm
from fabrica.models import Aluno, Campus, Curso
from django.views.generic.edit import CreateView
from .forms import CursoForm
from .models.Campus import Campus
from .models.Curso import Curso
from .models.Aluno import Aluno


def default(request):
    return render(request, 'index.html')

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm()

    return render(request, 'edit_Aluno/new_Aluno.html', {'form': form})


def lista_alunos(request):
    alunos = Aluno.objects.all()  # Recupera todos os alunos do banco de dados
    campus_filter = request.GET.get('campus')
    curso_filter = request.GET.get('curso')

    if campus_filter:
        alunos = alunos.filter(campus__nome=campus_filter)

    if curso_filter:
        alunos = alunos.filter(curso__nome=curso_filter)

    # Obtém as opções de campus e cursos para exibir nos filtros
    campus_options = Campus.objects.all()
    curso_options = Curso.objects.all()

    return render(request, 'listas/listar_Alunos.html', {
        'alunos': alunos,
        'campus_options': campus_options,
        'curso_options': curso_options,
        'campus_filter': campus_filter,
        'curso_filter': curso_filter,
    })

class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'edit_Aluno/newCurso.html'
    success_url = reverse_lazy('lista_alunos')

class CampusCreateView(CreateView):
    model = Curso
    form_class = CampusForm
    template_name = 'edit_Aluno/newCampus.html'
    success_url = reverse_lazy('lista_alunos')


def cursos_por_campus(request, campus_id):
    cursos = Curso.objects.filter(campus_id=campus_id).values('id', 'nome')
    return JsonResponse({'cursos': list(cursos)})