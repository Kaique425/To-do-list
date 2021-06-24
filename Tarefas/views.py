from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from  .models import Tarefas
# Create your views here.

class HomeList(ListView):
    model = Tarefas
    template_name= 'Tarefas/home_list.html'
