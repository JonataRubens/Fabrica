from datetime import date
from django.db import models


CURSO_CHOICES = [
        ('Engenharia de Software', 'Engenharia de Software'),
        ('Sistemas de Informação', 'Sistemas de Informação'),
        ('Ciências da Computação', 'Ciências da Computação'),
        # Adicione outros cursos conforme necessário
    ]

CAMPUS_CHOICES = [
    ('Palmas', 'Palmas'),
    ('Porto Nacional', 'Porto Nacional'),
    ('Arraias', 'Arraias'),
]

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
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    matricula = models.CharField(max_length=10, unique=True, editable=False)
    curso = models.CharField(max_length=50, choices=CURSO_CHOICES)
    campus = models.CharField(max_length=20, choices=CAMPUS_CHOICES)
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to='alunos_fotos/', blank=True, null=True)
    situacao = models.CharField(max_length=20, choices=SITUACAO_CHOICES)
    forma_ingresso = models.CharField(max_length=20, choices=FORMA_INGRESSO_CHOICES)
    data_ingresso = models.DateField(default=date.today)

    def save(self, *args, **kwargs):
        if not self.matricula:
            # Extrair ano e determinar semestre com base na data_ingresso
            ano = self.data_ingresso.strftime('%Y')
            semestre = '1' if self.data_ingresso.month <= 6 else '2'
            # Contar quantos alunos já existem para criar a sequência
            sequencia = Aluno.objects.count() + 1
            # Formatar a matrícula conforme a regra especificada
            self.matricula = f'{ano}{semestre}{str(sequencia).zfill(4)}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_completo} ({self.matricula})"
