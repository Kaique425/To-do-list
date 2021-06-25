from django.urls import path 
from .views import TarefasDetail, TarefasList, TarefasCreate, TarefasUpdate, TarefasDelete

urlpatterns = [
    path('', TarefasList.as_view(), name='listatarefa'),
    path('tarefa/<int:pk>',TarefasDetail.as_view(),name='detalhetarefa'),
    path('criar-tarefa', TarefasCreate.as_view(), name='criartarefa'),
    path('editar-tarefa/<int:pk>', TarefasUpdate.as_view(), name='editartarefa'),
    path('apagar-tarefa/<int:pk>', TarefasDelete.as_view(), name='apagartarefa'),
]