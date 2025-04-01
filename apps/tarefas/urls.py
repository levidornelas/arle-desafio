from django.urls import path
from .views import TarefaListView, TarefaCreateView, TarefaUpdateView, TarefaDeleteView

app_name = "tarefas"

urlpatterns = [
    path("", TarefaListView.as_view(), name="lista"),
    path("nova/", TarefaCreateView.as_view(), name="nova"),
    path("<int:pk>/editar/", TarefaUpdateView.as_view(), name="editar"),
    path("<int:pk>/excluir/", TarefaDeleteView.as_view(), name="excluir"),
]
