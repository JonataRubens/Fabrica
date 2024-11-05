from django.contrib import admin
from django.urls import include, path
from fabrica.views import lista_alunos
from .views import ViewRequests

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_alunos, name='index'),

    # path('new_aluno/', views.new_aluno, name='new_aluno')
    path('<str:folder_name>/<str:template_name>/', ViewRequests.as_view(), name='view_requests'),
]
#  src="{% static '' %}" alt="...">