from django.contrib import admin
from django.urls import include, path
from fabrica.views import lista_alunos
from .views import ViewRequests, cadastrarCurso, default
from fabrica import settings, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', default, name='index'),
    path('<str:folder_name>/<str:template_name>/', ViewRequests.as_view(), name='view_requests'),
    path('cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('cadastrarCurso/', cadastrarCurso, name='cadastrarCurso'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)