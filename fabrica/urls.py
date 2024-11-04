from django.contrib import admin
from django.urls import include, path
from fabrica.views import lista_alunos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_alunos, name='index'),
    
]
#  src="{% static '' %}" alt="...">