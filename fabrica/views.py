from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from fabrica.forms import AlunoForm



def lista_alunos(request):
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
            return redirect('index')
    else:
        form = AlunoForm()

    return render(request, 'edit_Aluno/new_Aluno.html', {'form': form})