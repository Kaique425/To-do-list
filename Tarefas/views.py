from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from  .models import Tarefas
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin



class UsuarioLoginView(LoginView):
    template_name='Tarefas/login.html'
    fields = ['titulo', 'descricao', 'completa']
    redirect_authenticated_user = True 

    
    def get_success_url(self):
        return reverse_lazy('listatarefa')

class TarefasList(LoginRequiredMixin,ListView):
    model = Tarefas
    context_object_name = 'Tarefas'
    template_name = 'Tarefas/tarefas_list.html'

    #Filtrar pro usuario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Tarefas'] = context['Tarefas'].filter(user=self.request.user)
        context['Count'] = context['Tarefas'].filter(completa=False).count()
        return context


class TarefasDetail(LoginRequiredMixin,DetailView):
    model = Tarefas
    context_object_name = 'Tarefas'


class TarefasCreate(LoginRequiredMixin,CreateView):
    model = Tarefas
    fields = ['titulo', 'descricao', 'completa']
    success_url = reverse_lazy('listatarefa')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TarefasCreate, self).form_valid(form)

class TarefasUpdate(LoginRequiredMixin,UpdateView):
    model = Tarefas
    fields = ['titulo', 'descricao', 'completa']
    success_url = reverse_lazy('listatarefa')


class TarefasDelete(LoginRequiredMixin,DeleteView):
    model = Tarefas
    success_url = reverse_lazy('listatarefa')
    context_object_name = 'Tarefas'