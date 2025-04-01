from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Tarefa

class TarefaListView(ListView):
    model = Tarefa
    template_name = "tarefas/lista.html"
    context_object_name = "tarefas"
    paginate_by = 5
    ordering = ['id']

class TarefaCreateView(CreateView):
    model = Tarefa
    fields = ["titulo", "descricao", "concluida", "categoria"]
    template_name = "tarefas/formulario.html"
    success_url = reverse_lazy("tarefas:lista")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Tarefa criada com sucesso!")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao criar a tarefa. Por favor, tente novamente.")
        return super().form_invalid(form)

class TarefaUpdateView(UpdateView):
    model = Tarefa
    fields = ["titulo", "descricao", "concluida", "categoria"]
    template_name = "tarefas/formulario.html"
    success_url = reverse_lazy("tarefas:lista")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Tarefa atualizada com sucesso!")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao atualizar a tarefa. Por favor, tente novamente.")
        return super().form_invalid(form)

class TarefaDeleteView(DeleteView):
    model = Tarefa
    template_name = "tarefas/confirmar_exclusao.html"
    success_url = reverse_lazy("tarefas:lista")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Tarefa excluída com sucesso!")
        return super().delete(request, *args, **kwargs)
