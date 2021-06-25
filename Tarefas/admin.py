from django.contrib import admin
from .models import Tarefas

# Register your models here.

@admin.register(Tarefas)
class TarefasAdmin(admin.ModelAdmin):
    list_display=('titulo',)
