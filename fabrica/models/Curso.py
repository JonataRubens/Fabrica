from django.db import models
from .Campus import Campus

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name="cursos")
    
    def __str__(self):
        return f"{self.nome} ({self.campus.nome})"