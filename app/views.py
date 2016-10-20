from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from app.forms import TarefaForm
from app.models import Tarefa

class TarefaView(TemplateView):
    template_name = "tarefa.html"
    
    def get_context_data(self, **kwargs):
        context = super(TarefaView, self).get_context_data(**kwargs)
        context['form'] = TarefaForm()

        # Faz o query de todas as instâncias de tarefa no banco de dados e adiciona ao contexto
        context['lista_de_tarefas'] = Tarefa.objects.all()
        return context

    def post(self, request, *args, **kwargs):

        # Altara o status da tarefa quando o botão de status é apertado
        if request.POST.__contains__('status'):
            tarefa = Tarefa.objects.get(pk=request.POST['status'])
            tarefa.mudar_status()

        # Apaga a tarefa quando o botão de apagar é apertado
        if request.POST.__contains__('apagar'):
            tarefa = Tarefa.objects.get(pk=request.POST['apagar'])
            tarefa.delete()

        # Cria uma nova tarefa quando o formulário de adicionar é enviado
        if request.POST.__contains__('nome'):
            form = TarefaForm(request.POST)
            if form.is_valid():
                form.save()
                
        return HttpResponseRedirect(reverse('tarefa'))
