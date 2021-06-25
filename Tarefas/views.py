from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from  .models import Tarefas
from django.urls import reverse_lazy


class TarefasList(ListView):
    model = Tarefas
    context_object_name = 'Tarefas'
    template_name= 'Tarefas/tarefas_list.html'


class TarefasDetail(DetailView):
    model = Tarefas
    context_object_name = 'Tarefas'


class TarefasCreate(CreateView):
    model = Tarefas
    fields = '__all__'
    success_url = reverse_lazy('listatarefa')

class TarefasUpdate(UpdateView):
    model = Tarefas
    fields = '__all__'
    success_url = reverse_lazy('listatarefa')


class TarefasDelete(DeleteView):
    model = Tarefas
    success_url = reverse_lazy('listatarefa')
    context_object_name = 'Tarefas'