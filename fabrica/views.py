from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from fabrica.forms import AlunoForm
from fabrica.models import Aluno, Campus, Curso


def default(request):
    return render(request, 'index.html')

class ViewRequests(TemplateView):

    def get_template_names(self):
        folder_name = self.kwargs['folder_name']
        template_name = self.kwargs['template_name']
        return [f'{folder_name}/{template_name}.html']
    


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