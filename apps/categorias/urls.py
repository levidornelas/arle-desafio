from django.urls import path
from .views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView

app_name = "categorias"  # Define o namespace do app

urlpatterns = [
    path("", CategoriaListView.as_view(), name="lista"),  # Listar categorias
    path("criar/", CategoriaCreateView.as_view(), name="criar"),  # Criar categoria
    path("editar/<int:pk>/", CategoriaUpdateView.as_view(), name="editar"),  # Editar categoria
    path("excluir/<int:pk>/", CategoriaDeleteView.as_view(), name="excluir"),  # Excluir categoria
]
