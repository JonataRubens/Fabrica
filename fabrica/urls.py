from django.contrib import admin
from django.urls import path
from fabrica.views import CursoCreateView, CampusCreateView
from .views import default
from fabrica import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', default, name='index'),
     path('cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    # path('<str:folder_name>/<str:template_name>/', ViewRequests.as_view(), name='view_requests'),


   ##################TEST##########################

    path('curso/add/', CursoCreateView.as_view(), name='cadastrarCurso'),
    path('campus/add/', CampusCreateView.as_view(), name='cadastrarCampus'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)