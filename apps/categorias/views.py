from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Categoria
from .forms import CategoriaForm

class CategoriaListView(ListView):
    model = Categoria
    template_name = "categorias/lista.html"
    context_object_name = "categorias"

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "categorias/formulario.html"
    success_url = reverse_lazy("categorias:lista")

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "categorias/formulario.html"
    success_url = reverse_lazy("categorias:lista")

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "categorias/confirmar_exclusao.html"
    success_url = reverse_lazy("categorias:lista")
