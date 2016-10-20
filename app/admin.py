from django.contrib import admin
from app.models import *

class TarefaAdmin(admin.ModelAdmin):
    list_display = []
    for field in Tarefa._meta.fields :
        list_display.append(field.name)

admin.site.register(Tarefa, TarefaAdmin)
