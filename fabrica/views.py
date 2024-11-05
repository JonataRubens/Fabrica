from django.shortcuts import render
from django.views.generic import TemplateView

def lista_alunos(request):
    return render(request, 'index.html')

class ViewRequests(TemplateView):

    def get_template_names(self):
        folder_name = self.kwargs['folder_name']
        template_name = self.kwargs['template_name']
        return [f'{folder_name}/{template_name}.html']