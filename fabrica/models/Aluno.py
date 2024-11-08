from datetime import date
from django.db import models
from .Curso import Curso
from .Campus import Campus

SITUACAO_CHOICES = [
    ('Vinculado', 'Vinculado'),
    ('Formado', 'Formado'),
    ('Jubilado', 'Jubilado'),
    ('Evadido', 'Evadido'),
]

FORMA_INGRESSO_CHOICES = [
    ('Vestibular', 'Vestibular'),
    ('SISU', 'SISU'),
    ('PSEnem', 'PSEnem'),
]

class Aluno(models.Model):
    nome_completo = models.CharField(max_length=255, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    matricula = models.CharField(max_length=10, unique=True, editable=False, verbose_name="Matrícula")
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name="alunos", verbose_name="Curso")
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT, related_name="alunos", verbose_name="Campus")
    data_nascimento = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")
    foto = models.ImageField(upload_to='alunos_fotos/', blank=True, null=True, verbose_name="Foto do Aluno")
    situacao = models.CharField(max_length=20, choices=SITUACAO_CHOICES, verbose_name="Situação")
    forma_ingresso = models.CharField(max_length=20, choices=FORMA_INGRESSO_CHOICES, verbose_name="Forma de Ingresso")
    data_ingresso = models.DateField(default=date.today, verbose_name="Data de Ingresso")

    def save(self, *args, **kwargs):
        if not self.matricula:
            ano = self.data_ingresso.strftime('%Y')
            semestre = '1' if self.data_ingresso.month <= 6 else '2'
            sequencia = Aluno.objects.count() + 1
            self.matricula = f'{ano}{semestre}{str(sequencia).zfill(4)}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_completo} ({self.matricula})"
