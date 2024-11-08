from django.contrib import admin
from .models import Aluno, Campus, Curso

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'matricula', 'curso', 'campus', 'situacao', 'forma_ingresso','data_ingresso')
    search_fields = ('nome_completo', 'cpf', 'matricula')
    list_filter = ('campus', 'situacao', 'forma_ingresso', )
    readonly_fields = ('matricula',)

    def save_model(self, request, obj, form, change):
        if not obj.matricula:  # Gera a matrícula automaticamente, se não existir
            obj.save()
        super().save_model(request, obj, form, change)


admin.site.register(Campus)
admin.site.register(Curso)