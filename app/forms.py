from django.forms import ModelForm
from app.models import *

class TarefaForm(ModelForm):

    
    class Meta:
        model = Tarefa
        fields = ['nome']
        labels = {
            'nome': '',
        }