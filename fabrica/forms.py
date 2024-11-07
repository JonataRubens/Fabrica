from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome_completo', 'cpf', 'curso', 'campus', 'data_nascimento', 'foto', 'situacao', 'forma_ingresso']



    