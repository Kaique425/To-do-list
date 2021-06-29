from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from  .models import Tarefas

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class UsuarioLoginView(LoginView):
    template_name='Tarefas/login.html'
    fields = ['titulo', 'descricao', 'completa']
    redirect_authenticated_user = True 

    
    def get_success_url(self):
        return reverse_lazy('listatarefa')


class RegistrarFormView(FormView):
    template_name = 'Tarefas/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('listatarefa')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistrarFormView, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('listatarefa')
        return super(RegistrarFormView, self).get(*args, **kwargs)


class TarefasList(LoginRequiredMixin,ListView):
    model = Tarefas
    context_object_name = 'Tarefas'
    template_name = 'Tarefas/tarefas_list.html'

    #Filtrar por usuario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Tarefas'] = context['Tarefas'].filter(user=self.request.user)
        context['Count'] = context['Tarefas'].filter(completa=False).count()
        
        procura_input = self.request.GET.get("area-de-procura") or ''
        if procura_input:
            context['Tarefas'] = context['Tarefas'].filter(titulo__istartswith=procura_input)
        
        context['procura_input'] = procura_input

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