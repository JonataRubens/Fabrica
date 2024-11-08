# fabrica/forms.py

from django import forms
from .models.Campus import Campus
from .models.Curso import Curso
from .models.Aluno import Aluno

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['nome']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'campus']

    campus = forms.ModelChoiceField(queryset=Campus.objects.all(), empty_label="Selecione o Campus", required=True)

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'nome_completo', 'cpf', 'curso', 'campus', 
            'data_nascimento', 'foto', 'situacao', 'forma_ingresso'
        ]
